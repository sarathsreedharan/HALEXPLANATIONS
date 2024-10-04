import argparse
import sys
import pddlpy
import yaml
import os
import copy
import numpy
import itertools
import time
from Search import *

OPERATOR_DEFN_KEYS = ['precondition_pos','precondition_neg', 'effect_pos', 'effect_neg']
PLANNER_COMMAND = '/media/data_mount/mycode/EXPABS/src/predicate_abs/fdplan.sh {} {}'
ACTION_DEF_STR = '(:action {}\n:parameters ({})\n:precondition\n(and\n{}\n)\n:effect\n(and\n{}\n)\n)\n'
VAL_COMMAND = '/media/data_mount/mycode/EXPABS/src/predicate_abs/valplan.sh {} {} {}'

FOIL_DETECTION_LIMIT = 20
LATTICE_GEN_LIMIT = 80

class Lattice:
    def __init__(self, domain_model, problem, perc_of_predicates, min_height, lattice_dest,
                 foil_dest, domain_dest, problem_dest, dom_templ, prob_templ, foil_count):
        self.dom_prob = pddlpy.DomainProblem(domain_model, problem)
        self.get_lifted_dom_prob_dict()
#        self.no_of_predicates = no_of_predicates
        self.perc_of_predicates = (perc_of_predicates/100.00)
        self.preds_list = self.get_random_predicates()
        self.foil_count = foil_count
        # finised upto
        print ("self.perc_of_predicates",self.perc_of_predicates)
        print ("Creating a lattice with predicates",self.preds_list)
        #exit(0)
        self.domain_model = domain_model
        self.problem = problem
        self.min_height = min_height
        self.initial_node = "c1"
        self.lattice_dest = lattice_dest
        self.foil_dest = foil_dest
        with open(dom_templ) as d_fd:
            self.domain_template_str = d_fd.read().strip()
        with open(prob_templ) as p_fd:
            self.prob_template_str = p_fd.read().strip()
        self.dom_dest = domain_dest
        self.prob_dest = problem_dest

    def convert_pred_tuple_list(self, orig_prop_list, skip_list = []):
        prop_list = set()
        for p in orig_prop_list:
            #print (p)
            if type(p) is tuple:
                prop = ' '.join([str(i) for i in p])
            else:
                prop = ' '.join([str(i) for i in p.predicate])
            #print ("prop",prop)
            if prop not in skip_list:
                prop_list.add(prop)
        return prop_list 

    def get_lifted_dom_prob_dict(self):
        self.orig_dom = {}
        self.orig_dom['init_state'] = self.convert_pred_tuple_list(self.dom_prob.initialstate())
        self.orig_dom['goal_state'] = self.convert_pred_tuple_list(self.dom_prob.goals())
        act_map = {}
        #print (self.dom_prob.vargroundspace)
        for act in list(self.dom_prob.operators()):
            #print (act_obj.variable_list)
            #print (self.dom_prob.vargroundspace)
            print ("act",act)
            print ("var list",self.dom_prob.domain.operators[act].variable_list.keys())
            sorted_var_name = list(self.dom_prob.domain.operators[act].variable_list.keys())
            sorted_var_name.sort()
            para_list = [ k + " - " + self.dom_prob.domain.operators[act].variable_list[k] for k in sorted_var_name]
            action_name = act
            act_map[action_name] = {}
            act_map[action_name]['parameters'] = " ".join(para_list)
            act_map[action_name]['precondition_pos'] = self.convert_pred_tuple_list(self.dom_prob.domain.operators[act].precondition_pos)
            act_map[action_name]['precondition_neg'] = self.convert_pred_tuple_list(self.dom_prob.domain.operators[act].precondition_neg)
            act_map[action_name]['effect_pos'] = self.convert_pred_tuple_list(self.dom_prob.domain.operators[act].effect_pos)
            act_map[action_name]['effect_neg'] = self.convert_pred_tuple_list(self.dom_prob.domain.operators[act].effect_neg)

            print ("parameter",act_map[action_name]['parameters'])
        self.orig_dom['actions'] = act_map

    def get_random_predicates(self):
        # Collect the set of all propositions
        predicates_set = set() 
        for a in self.orig_dom['actions'].keys():
            tmp_set = self.orig_dom['actions'][a]['precondition_pos'] | self.orig_dom['actions'][a]['precondition_neg']\
                    |self.orig_dom['actions'][a]['effect_pos'] | self.orig_dom['actions'][a]['effect_neg']
            for i in tmp_set:
                # This is only for depot
                if i.split(' ')[0].lower() != 'on':
                    predicates_set.add(i.split(' ')[0])
        pred_list = list(predicates_set)
        #print ("prop list",prop_list)
        print ("len pred list",len(pred_list))
        # Shuffle to get k random propositions
        self.no_of_predicates = int(len(pred_list)*self.perc_of_predicates)
        rand = numpy.random.RandomState()
        rand.shuffle(pred_list)
        random_preds = pred_list[:self.no_of_predicates]
        #gl = list(self.convert_pred_tuple_list(self.dom_prob.goals()))
        #rand.shuffle(gl)
        #random_preds[0] = gl[0]
        return random_preds

    def get_all_possible_nodes(self):
        # All possible nodes for the lattice
        power_set = []
        for i in range(1,len(random_props)+1):
            power_set += list(itertools.combinations(random_props,i))        
        # Generate the lattice
        return power_set

    def add_all_edges(self, lattice_map, curr_node):
        if curr_node == '':
            return lattice_map
        cl_list = curr_node.split('@')
        #print (len(cl_list))
        for p in cl_list:
            rem = list(set(cl_list) - set([p]))
            if len(rem) == 0:
                parent_node = ''
            else:
                rem.sort()
                parent_node = "@".join(rem)
            curr_path = lattice_map['curr_path'][curr_node] - 1
            if parent_node in lattice_map['curr_path'].keys():
                if lattice_map['curr_path'][parent_node] < curr_path:
                    lattice_map['curr_path'][parent_node] = curr_path
            else:
                lattice_map['curr_path'][parent_node] = curr_path
            if parent_node not in lattice_map['inverse_edges'].keys():#len(parent_node.split('@')) == lattice_map['inverse_edges'][parent_node]:
                lattice_map = self.add_all_edges(lattice_map, parent_node)
            if parent_node not in lattice_map['edges'].keys():
                lattice_map['edges'][parent_node] = []
            if curr_node not in lattice_map['edges'][parent_node]:
                lattice_map['edges'][parent_node].append(curr_node)
            if curr_node not in lattice_map['inverse_edges'].keys():
                lattice_map['inverse_edges'][curr_node] = [parent_node]
            elif parent_node not in lattice_map['inverse_edges'][curr_node]:
                lattice_map['inverse_edges'][curr_node].append(parent_node)
            if parent_node != '':
                lattice_map['nodes'].add(parent_node)
            lattice_map['leaf_nodes'].add(parent_node)
            lattice_map['used_propositions'].add(p)
        return lattice_map
        

    def get_all_successor_nodes(self, node_obj):
        successor_list = []
        curr_lattice_map = node_obj.current_state
        for p in self.preds_list:
            leaf_node_list = list(curr_lattice_map['leaf_nodes'])
            #print (leaf_node_list)
            for node in leaf_node_list:
                if p not in node.split('@'): # and curr_lattice_map['curr_path'][node] < self.min_height:
                    tmp_lattice_map = copy.deepcopy(curr_lattice_map)
                    if node != '':
                        nl = node.split('@') + [p]
                        nl.sort()
                        curr_node = '@'.join(nl )
                    else:
                        curr_node = p
                    #tmp_lattice_map['leaf_nodes'].remove(node)
                    tmp_lattice_map['leaf_nodes'].add(curr_node)
                    tmp_lattice_map['nodes'].add(curr_node)
                    
                    #if curr_node not in tmp_lattice_map['edges'].keys():
                    #    tmp_lattice_map['edges'][curr_node] = []
                    #if curr_node not in tmp_lattice_map['edges'][node]:
                    #    tmp_lattice_map['edges'][node].append(curr_node)
                    #if curr_node not in tmp_lattice_map['inverse_edges'].keys():
                    #    tmp_lattice_map['inverse_edges'][curr_node] = [node]
                    #elif node not in tmp_lattice_map['inverse_edges'][curr_node]:
                    #    tmp_lattice_map['inverse_edges'][curr_node].append(node)

                    curr_path = tmp_lattice_map['curr_path'][node] + 1
                    if curr_node in tmp_lattice_map['curr_path'].keys():
                        if tmp_lattice_map['curr_path'][curr_node] < curr_path:
                            tmp_lattice_map['curr_path'][curr_node] = curr_path
                    else:
                        tmp_lattice_map['curr_path'][curr_node] = curr_path

                    if curr_path > tmp_lattice_map['longest_path']:
                        tmp_lattice_map['longest_path'] = curr_path

                    tmp_lattice_map['used_propositions'].add(p)
                    tmp_lattice_map = self.add_all_edges(tmp_lattice_map, curr_node)
                    successor_list.append(LatNode(self, tmp_lattice_map, node_obj.plan + [p]))
        #print (successor_list)
        return successor_list


    

    def create_the_lattice(self):
        prob_completed = False
        prob_start_time = time.time()
        while not prob_completed and (time.time() - prob_start_time) < LATTICE_GEN_LIMIT:
            self.preds_list = self.get_random_predicates()
            init_map = {}
            init_map['init'] = ''
            init_map['leaf_nodes'] = set()
            init_map['leaf_nodes'].add('')
            init_map['edges'] = {'':[]}
            init_map['inverse_edges'] = {}
            init_map['longest_path'] = 0
            init_map['nodes'] = set()
            init_map['curr_path'] = {}
            init_map['curr_path'][''] = 0
            init_map['used_propositions'] = set()
            all_last_level_nodes = ['@'.join(sorted(list(i))) for i in list(itertools.combinations(self.preds_list, len(self.preds_list)))]
            rand = numpy.random.RandomState()
            rand.shuffle(all_last_level_nodes)
            l = rand.randint(1,len(all_last_level_nodes)+1)
            most_abstract_nodes = copy.deepcopy(all_last_level_nodes[:l])
            print ("DEBUG: All possible last level nodes",all_last_level_nodes)
            print ("DEBUG: Most abstract nodes",most_abstract_nodes)
            for curr_node in most_abstract_nodes:
                init_map['leaf_nodes'].add(curr_node)
                init_map['nodes'].add(curr_node)
                node_parts = curr_node.split('@')
                for p in node_parts:
                    init_map['used_propositions'].add(p)
                init_map['curr_path'][curr_node] = len(node_parts)
                if len(node_parts) > init_map['longest_path']:
                    init_map['longest_path'] = len(node_parts)
                init_map = self.add_all_edges(init_map, curr_node)
            if not self.verify_the_lattice(init_map):
                print ("Oh Oh")
                exit(1)
            self.dump_lattice_yaml(init_map)
            print ("Lattice created..")
            print ("creating foil...")
            exit(0)
            st = self.create_foil(init_map)
            if st:
                self.create_domain_problem('', self.dom_dest, self.prob_dest )
                print ("Foil created ...")
                prob_completed = True



    def verify_the_lattice(self, lattice_dict):
        # All nodes have the same number of incoming nodes as the propositions that have been removed
        i = 0
        for n in lattice_dict['nodes']:
            missing_preds = n.split('@')
            if len(missing_preds)  != len(lattice_dict['inverse_edges'][n]):
                i+=1
        #print ("the lat not satisfied for",i)
        if i > 0:
            return False
        #else:
        #    print ("Node is ",lattice_dict["edges"])
        # Make sure that the longest path with in the lattice is greater than the min height
        if lattice_dict['longest_path'] < self.min_height:
            #if i == 0:
                #print  ("Not long enough",lattice_dict['longest_path'])
            return False

        # Make Sure all the propositions are used
        if len(lattice_dict['used_propositions']) != len(self.preds_list):
            #if i == 0:
                #print  ("Not prop enough")

            return False

        return True

    def dump_lattice_yaml(self, lattice_state):
        final_lattice = { 'Lattice': {}}
        final_lattice['Lattice']['Init'] = 'c1'
        curr_ind = 2
        final_lattice['Lattice']['Nodes'] = []
        self.node_map = {'':'c1'}
        for i in lattice_state['nodes']:
            curr_node = "c"+str(curr_ind)
            final_lattice['Lattice']['Nodes'].append(curr_node)
            self.node_map[i] = curr_node
            curr_ind += 1
        #print ("node map",self.node_map)
        final_lattice['Lattice']['Edges'] = []
        #print ("edges",lattice_state['edges'])
        #print ("inv edges",lattice_state['inverse_edges'])
        for e in lattice_state['edges'].keys():
            for e2 in lattice_state['edges'][e]:
                node_name =list(set(e2.split('@')) - set(e.split('@')))[0]
                final_lattice['Lattice']['Edges'].append([self.node_map[e], node_name, self.node_map[e2]])
        with open(self.lattice_dest, 'w') as l_fd:
            yaml.dump(final_lattice, l_fd)

    def create_domain_problem(self, node, dom_dest, prob_dest):
        act_map = {}
        problem_map = {}
        ground_action = []
        if node == '':
            pred_list = []
        else:
            pred_list = node.split('@')
         
        for action_name in self.orig_dom['actions'].keys():
            #
            act_map[action_name] = {}
            act_map[action_name]['parameters'] = self.orig_dom['actions'][action_name]['parameters']
            act_map[action_name]['precondition_pos'] = set( )
            for x in self.orig_dom['actions'][action_name]['precondition_pos']:
                if x.split(' ')[0] not in pred_list:
                    act_map[action_name]['precondition_pos'].add(x)

            act_map[action_name]['precondition_neg'] = set()
            for x in self.orig_dom['actions'][action_name]['precondition_neg']:
                if x.split(' ')[0] not in pred_list:
                    act_map[action_name]['precondition_neg'].add(x)

            act_map[action_name]['effect_pos'] = set()
            for x in self.orig_dom['actions'][action_name]['effect_pos']:
                if x.split(' ')[0] not in pred_list:
                    act_map[action_name]['effect_pos'].add(x)

            act_map[action_name]['effect_neg'] = set()
            for x in self.orig_dom['actions'][action_name]['effect_neg']:
                if x.split(' ')[0] not in pred_list:
                    act_map[action_name]['effect_pos'].add(x)

        action_strings = []

        for i in  act_map.keys():
            precondition_list = ['('+i+')' for i in act_map[i]['precondition_pos']]
            precondition_list += ['(not ('+i+'))' for i in act_map[i]['precondition_neg']]
            effect_list = ['('+i+')' for i in act_map[i]['effect_pos']]
            effect_list += ['(not ('+i+'))' for i in act_map[i]['effect_neg']]

            action_strings.append(ACTION_DEF_STR.format(i, act_map[i]['parameters'],"\n".join(precondition_list),"\n".join(effect_list)))
        dom_str = self.domain_template_str.format("\n".join(action_strings))

        curr_goal_state = set()
        curr_init_state = set()

        for x in self.orig_dom['init_state']:
            if x.split(' ')[0] not in pred_list:
                curr_init_state.add(x)

        for x in self.orig_dom['goal_state']:
            if x.split(' ')[0] not in pred_list:
                curr_goal_state.add(x)

        goal_state_str_list = ['('+i+')' for i in curr_goal_state]
        init_state_str_list = ['('+i+')' for i in curr_init_state]

        prob_str = self.prob_template_str.format("\n".join(init_state_str_list), "\n".join(goal_state_str_list))

        with open(dom_dest, 'w') as d_fd:
            d_fd.write(dom_str)

        with open(prob_dest, 'w') as p_fd:
            p_fd.write(prob_str)



    def find_plan(self, node):
        tmp_domain = "/tmp/domain.pddl"
        tmp_problem = "/tmp/problem.pddl"
        self.create_domain_problem(node, tmp_domain, tmp_problem)
        print ("command",PLANNER_COMMAND.format(tmp_domain, tmp_problem))
        output_plan = [i.strip() for i in os.popen(PLANNER_COMMAND.format(tmp_domain, tmp_problem)).read().strip().split('\n')]
        # Because of an error on FF
        plan_file = "/tmp/plan_test.sol"
        with open(plan_file, 'w') as p_fd:
            p_fd.write("\n".join(output_plan))
        output = [i.strip() for i in os.popen(VAL_COMMAND.format(tmp_domain, tmp_problem, plan_file)).read().strip().split('\n')]
        if eval(output[0]):
            return output_plan
        else:
            return ""

    def test_on_original_model(self, plan):
        tmp_domain = "/tmp/domain.pddl"
        tmp_problem = "/tmp/problem.pddl"
        self.create_domain_problem('', tmp_domain, tmp_problem)
        plan_file = "/tmp/plan.sol"
        with open(plan_file, 'w') as p_fd:
                p_fd.write("\n".join(plan))
        print (VAL_COMMAND.format(tmp_domain, tmp_problem, plan_file))
        output = [i.strip() for i in os.popen(VAL_COMMAND.format(tmp_domain, tmp_problem, plan_file)).read().strip().split('\n')]
        return eval(output[0])

    def create_foil(self, lattice_map):
        foil_found = False
        original_plan = "@".join(self.find_plan(''))
        curr_nodes = list(copy.deepcopy(lattice_map["nodes"]))
        #print ("original_plan",original_plan)
        #print ("foil cocun", self.foil_count)
        found_foil_count = 0
        foil_list = []
        start_time = time.time()
        while not foil_found and (time.time() - start_time) < FOIL_DETECTION_LIMIT:
            # sample nodes
            rand = numpy.random.RandomState()
            r_id = rand.randint(0,len(curr_nodes))
            node = curr_nodes[r_id]
            poss_foil = self.find_plan(node)
            #print ("poss_foil", poss_foil)
            if "@".join(poss_foil) != original_plan and "@".join(poss_foil) != "" and "@".join(poss_foil) not in foil_list and not self.test_on_original_model(poss_foil):
                found_foil_count += 1
                #print ("poss_foil", poss_foil)
                with open(self.foil_dest + str(found_foil_count),'w') as f_fd:
                    f_fd.write("\n".join(poss_foil))
                    foil_list.append("@".join(poss_foil))
                    #print ("Writing to foil",self.foil_dest + str(found_foil_count))
            else:
                curr_nodes.remove(node)
            if found_foil_count == self.foil_count:
                foil_found = True
            if len(curr_nodes) == 0:
                return False
        if foil_found:
            return True
        else:
            return False

def main():
    parser = argparse.ArgumentParser(description='''The driver Script for the Explanation generation''',
                                     epilog="Usage >> ./Explainer.py -d ../domain/original_domain.pddl -p" +
                                            " ../domain/original_problem.pddl -f ../domain/foil.sol")
    '''
        # Flags
        --generate_lattice
    '''
    parser.add_argument('-d', '--domain_model',   type=str, help="Domain file with real PDDL model of robot.", required=True)
    parser.add_argument('-p', '--problem', type=str, help="Problem file for robot.", required=True)
    parser.add_argument('-n', '--no_of_predicates', type=str, help="No of predicates")
    parser.add_argument('-m', '--min_height', type=str, help="Min height for the lattice")
    parser.add_argument('-t', '--domain_dest', type=str, help="Domain file destination")
    parser.add_argument('-q', '--problem_dest', type=str, help="Problem file destination")
    parser.add_argument('-l', '--lattice_dest', type=str, help="Lattice yaml destination")
    parser.add_argument('-f', '--foil_dest', type=str, help="Foil solution destination")
    parser.add_argument('-r', '--domain_templ', type=str, help="Domain template file")
    parser.add_argument('-s', '--prob_templ', type=str, help="Problem template file")
    parser.add_argument('-c', '--foil_count', type=str, help="Foil count")

    if not sys.argv[1:] or '-h' in sys.argv[1:]:
        print (parser.print_help())
        sys.exit(1)
    args = parser.parse_args()
    

    lat = Lattice(args.domain_model, args.problem, int(args.no_of_predicates), int(args.min_height),
            args.lattice_dest, args.foil_dest, args.domain_dest, args.problem_dest, args.domain_templ,
            args.prob_templ, int(args.foil_count))
    lat.create_the_lattice()


if __name__ == "__main__":
    main()
