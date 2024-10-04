import argparse
import sys
import pddlpy
import yaml
import os
import copy
import numpy
import itertools
from Search import *

OPERATOR_DEFN_KEYS = ['precondition_pos','precondition_neg', 'effect_pos', 'effect_neg']
PLANNER_COMMAND = './fdplan.sh {} {}'
ACTION_DEF_STR = '(:action {}\n:parameters ()\n:precondition\n(and\n{}\n)\n:effect\n(and\n{}\n)\n)\n'
class Lattice:
    def __init__(self, domain_model, problem, no_of_propositions, min_height, lattice_dest,
                 foil_dest, domain_dest, problem_dest, dom_templ, prob_templ):
        self.dom_prob = pddlpy.DomainProblem(domain_model, problem)
        self.get_dom_prob_dict()
        self.no_of_propositions = no_of_propositions
        self.props_list = self.get_random_propositions()
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

    def convert_prop_tuple_list(self, orig_prop_list, skip_list = []):
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

    def get_dom_prob_dict(self):
        self.orig_dom = {}
        self.orig_dom['init_state'] = self.convert_prop_tuple_list(self.dom_prob.initialstate())
        self.orig_dom['goal_state'] = self.convert_prop_tuple_list(self.dom_prob.goals())
        act_map = {}
        #print (self.dom_prob.vargroundspace)
        for act in list(self.dom_prob.operators()):
            for act_obj in list(self.dom_prob.ground_operator(act)):
                #print (act_obj.variable_list)
                #print (self.dom_prob.vargroundspace)
                sorted_var_name = list(act_obj.variable_list.keys())
                sorted_var_name.sort()
                action_name_raw = act_obj.operator_name + "_" + '_'.join(act_obj.variable_list[i] for i in sorted_var_name)
                action_name = action_name_raw.lower()
                act_map[action_name] = {}
                act_map[action_name]['precondition_pos'] = self.convert_prop_tuple_list(act_obj.precondition_pos)
                act_map[action_name]['precondition_neg'] = self.convert_prop_tuple_list(act_obj.precondition_neg)
                act_map[action_name]['effect_pos'] = self.convert_prop_tuple_list(act_obj.effect_pos)
                act_map[action_name]['effect_neg'] = self.convert_prop_tuple_list(act_obj.effect_neg)

        self.orig_dom['actions'] = act_map

    def get_random_propositions(self):
        # Collect the set of all propositions
        proposition_set = set() 
        for i in  self.orig_dom['init_state']\
                | self.orig_dom['goal_state']:
            proposition_set.add(i)
        for a in self.orig_dom['actions'].keys():
            tmp_set = self.orig_dom['actions'][a]['precondition_pos'] | self.orig_dom['actions'][a]['precondition_neg']\
                    |self.orig_dom['actions'][a]['effect_pos'] | self.orig_dom['actions'][a]['effect_neg']
            for i in tmp_set:
                proposition_set.add(i)
        prop_list = list(proposition_set)
        #print ("prop list",prop_list)
        # Shuffle to get k random propositions
        rand = numpy.random.RandomState()
        rand.shuffle(prop_list)
        random_props = prop_list[:self.no_of_propositions]
        gl = list(self.convert_prop_tuple_list(self.dom_prob.goals()))
        rand.shuffle(gl)
        random_props[0] = gl[0]
        return random_props

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
        for p in self.props_list:
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
        init_node = LatNode(self, init_map)
        final_lat = BFSSearch(init_node)
        self.dump_lattice_yaml(final_lat.current_state)
        self.create_foil(final_lat.current_state)
        self.create_domain_problem('', self.dom_dest, self.prob_dest )

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
        if len(lattice_dict['used_propositions']) != len(self.props_list):
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
         
        for act in self.dom_prob.operators():
            for act_obj in list(self.dom_prob.ground_operator(act)):
                sorted_var_name = list(act_obj.variable_list.keys())
                sorted_var_name.sort()
                action_name = act_obj.operator_name + "_" + '_'.join(act_obj.variable_list[i] for i in sorted_var_name)
                act_map[action_name] = {}
                act_map[action_name]['precondition_pos'] = self.convert_prop_tuple_list(act_obj.precondition_pos, pred_list)
                act_map[action_name]['precondition_neg'] = self.convert_prop_tuple_list(act_obj.precondition_neg, pred_list)
                act_map[action_name]['effect_pos'] = self.convert_prop_tuple_list(act_obj.effect_pos, pred_list)
                act_map[action_name]['effect_neg'] = self.convert_prop_tuple_list(act_obj.effect_neg, pred_list)

        action_strings = []

        for i in  act_map.keys():
            precondition_list = ['('+i+')' for i in act_map[i]['precondition_pos']]
            precondition_list += ['(not ('+i+'))' for i in act_map[i]['precondition_neg']]
            effect_list = ['('+i+')' for i in act_map[i]['effect_pos']]
            effect_list += ['(not ('+i+'))' for i in act_map[i]['effect_neg']]

            action_strings.append(ACTION_DEF_STR.format(i,"\n".join(precondition_list),"\n".join(effect_list)))
        dom_str = self.domain_template_str.format("\n".join(action_strings))


        self.goal_state = ['('+i+')' for i in self.convert_prop_tuple_list(self.dom_prob.goals())]
        self.init_state = ['('+i+')' for i in self.convert_prop_tuple_list(self.dom_prob.initialstate())]

        prob_str = self.prob_template_str.format("\n".join(self.init_state), "\n".join(self.goal_state))

        with open(dom_dest, 'w') as d_fd:
            d_fd.write(dom_str)
        with open(prob_dest, 'w') as p_fd:
            p_fd.write(prob_str)



    def find_plan(self, node):
        tmp_domain = "/tmp/domain.pddl"
        tmp_problem = "/tmp/problem.pddl"
        self.create_domain_problem(node, tmp_domain, tmp_problem)
        output = [i.strip() for i in os.popen(PLANNER_COMMAND.format(tmp_domain, tmp_problem)).read().strip().split('\n')]
        return output

    def create_foil(self, lattice_map):
        foil_found = False
        original_plan = "@".join(self.find_plan(''))
        curr_nodes = list(copy.deepcopy(lattice_map["nodes"]))
        while not foil_found:
            # sample nodes
            rand = numpy.random.RandomState()
            rand.shuffle(curr_nodes)
            node = curr_nodes[0]
            poss_foil = self.find_plan(node)
            if "@".join(poss_foil) != original_plan and "@".join(poss_foil) != "":
                foil_found = True
                with open(self.foil_dest,'w') as f_fd:
                    f_fd.write("\n".join(poss_foil))
        


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
    parser.add_argument('-n', '--no_of_propositions', type=str, help="No of propositions")
    parser.add_argument('-m', '--min_height', type=str, help="Min height for the lattice")
    parser.add_argument('-t', '--domain_dest', type=str, help="Domain file destination")
    parser.add_argument('-q', '--problem_dest', type=str, help="Problem file destination")
    parser.add_argument('-l', '--lattice_dest', type=str, help="Lattice yaml destination")
    parser.add_argument('-f', '--foil_dest', type=str, help="Foil solution destination")
    parser.add_argument('-r', '--domain_templ', type=str, help="Domain template file")
    parser.add_argument('-s', '--prob_templ', type=str, help="Problem template file")

    if not sys.argv[1:] or '-h' in sys.argv[1:]:
        print (parser.print_help())
        sys.exit(1)
    args = parser.parse_args()
    

    lat = Lattice(args.domain_model, args.problem, int(args.no_of_propositions), int(args.min_height),
            args.lattice_dest, args.foil_dest, args.domain_dest, args.problem_dest, args.domain_templ,
            args.prob_templ)
    lat.create_the_lattice()


if __name__ == "__main__":
    main()
