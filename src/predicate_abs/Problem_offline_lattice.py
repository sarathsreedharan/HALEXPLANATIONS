import sys
import re
import os
import yaml
import pddlpy
import copy
import itertools
from Search import *
from ParseDck import *

PLANNER_COMMAND = './fdplan.sh {} {}'
VAL_COMMAND = './valplan.sh {} {} {}'
LAND_COMMAND = './generate_landmarks.sh {} {}'
ACTION_DEF_STR = '(:action {}\n:parameters ({})\n:precondition\n(and\n{}\n)\n:effect\n(and\n{}\n)\n)\n'
CHECK_PREV_OBS_ACT = '(:action CHECK_PREV_OBS\n:parameters ({})\n:precondition\n(and\n{}\n)\n:effect\n(and\n {} \n)\n)\n'
CHECK_OBS_SEQ = '(:action OBS_SEQ_COMPLETED_CHECK\n:parameters ({})\n:precondition\n(and\n{}\n)\n:effect\n(and\n (goal_completed) \n)\n)\n'

# Landmark compilation stuff
LANDMARK_OBS_ACT = "CHECK_LANDMARK_"
LANDMARK_GREEDY_NEC = "GREEDY_NEC_LAND_"
LANDMARK_NAT = "GREEDY_NAT_"
LANDMARK_ACHIEVED = "ACHIEVED_LANDMARK_"
GREEDY_NEC = "gn"
NAT_ORD = "nat"
LANDMARK_FIRST_TIME = 'FIRST_TIME_'
LANDMARK_NOTSET = 'NOTSET_'
LANDMARK_GOAL_CHECK = "LANDMARK_GOAL_TEST_"
LAND_CONJ_STR = "1V1"



TEST_CONDITION_ACTION = '(:action TEST_CONDITION_FOR_{}\n:parameters ({})\n:precondition\n(and\n{}\n)\n:effect\n(and\n {} \n)\n)\n'


AUT_STATE_PROP = "in_state_"

ENFORCE_ORDERING_PRED = 'enforce_ordering'
OBSERVED_PRED_PREFIX = 'observed_'
OBSERVED_ACT_PREFIX = 'act_observed_'
NEW_GOAL_PRED = "(goal_completed)"

WHILE_TEST_PREFIX = "WHILEtest"
WHILE_COND_SUCC = "WHILE_COND_SUCC"
WHILE_END = "END_OF_WHILE_LOOP"

IF_TEST_PREFIX = "IFtest"
IF_COND_SUCC = "IFBLOCK"
ELSE_BLOCK = "ELSEBLOCK"
END_IF = "END_CONDITION"

ND_CHOICE = "ND("
ND_REPEAT="*"
ANY_PREFIX="any"


def parse_land_line(orig_line, relative = False):
    line = re.sub('^LM \d Atom','StAtom',orig_line)
    PARSE_STR = "Atom "
    CONJ_STR = "CONJ"
    if 'conj {Atom ' not in line:
        atom = line.split(PARSE_STR)[-1].split(' (')[0].replace('(',' ').replace(',',' ').replace(')','')
    else:
        atom_list = []
        for atm_strs in line.split(CONJ_STR)[-1].split(', Atom '):
            if PARSE_STR in atm_strs:
                atom_list.append(atm_strs.split(PARSE_STR)[-1].split(' (')[0].split(' (')[0].replace('(',' ').replace(',',' ').replace(')',''))
            else:
                atom_list.append(atm_strs.split('conj {Atom ')[-1].split(' (')[0].split(' (')[0].replace('(',' ').replace(',',' ').replace(')',''))
        atom = LAND_CONJ_STR.join(atom_list)
    ld_type = "curr"
    if relative:
        if 'gn ' in line:
            ld_type = "gn"
        else:
            ld_type = "nat"
    return (atom, ld_type)

def parse_landmark_file(lfile):
    with open(lfile) as l_fd:
        land_content = [re.sub(r'var\d+\(\d+\)->\d+', '', l.strip()) for l in l_fd.readlines()]
    ind = 0
    parent_map = {}
    child_map = {}
    while ind < len(land_content):
        new_land = []
        curr_atom, ld_type = parse_land_line(land_content[ind])
        if curr_atom not in parent_map:
            parent_map[curr_atom] = {'gn':set(), 'nat':set()}
            child_map[curr_atom] = {'gn':set(), 'nat':set()}
        ind += 1
        while ind < len(land_content) and ('<-' in land_content[ind] or '->' in land_content[ind]):
            #print (land_content[ind])
            next_atom, order_type = parse_land_line(land_content[ind], relative=True)
            if '<-' in land_content[ind]:
                parent_map[curr_atom][order_type].add(next_atom)
            else:
                child_map[curr_atom][order_type].add(next_atom)
            ind+=1

    return (parent_map, child_map)




class Problem:

    def __init__(self, domain_model, problem, foil_prefix, foil_count, lattice_file,
                 dom_templ, prob_templ, search_type):
        self.lattice_file = lattice_file
        dom_prob = pddlpy.DomainProblem(domain_model, problem)
        self.search_type = search_type

        #print ("domain model")
        #print ("init state")
        self.resolved_models = {}
        self.predicate_type_map = {}

        self.orig_start = self.convert_prop_tuple_list(dom_prob.initialstate())
        #print ("goal state")
        self.goal_state = self.convert_prop_tuple_list(dom_prob.goals())
        self.orig_dom_map = self.convert_domain_obj_map(dom_prob)
        self.concret_costs = {}
        self.generate_lattice_from_file()

        # Assume a single foil
        self.foil_dck_obj = DCKParser(foil_prefix+'1')
        self.foil = [self.foil_dck_obj]
        #for f in range(1,int(foil_count)+1):
        #    foil_file = foil_prefix + str(f)
        #    with open(foil_file) as f_fd:
        #        self.foil.append([i.strip() for i in f_fd.readlines()])
        with open(dom_templ) as d_fd:
            self.domain_template_str = d_fd.read().strip()
        with open(prob_templ) as p_fd:
            self.prob_template_str = p_fd.read().strip()

        print ("MAP",self.predicate_type_map)
        #exit(0)

    def return_action_map_template(self):
        test_map = {}
        test_map['parameters'] = ""
        test_map['precondition_pos'] = set()
        test_map['precondition_neg'] = set()
        test_map['effect_pos'] = set()
        test_map['effect_neg'] = set()

        test_map['precondition_pos'].add(ENFORCE_ORDERING_PRED)
        return test_map



    def convert_prop_tuple_list(self, orig_prop_list, para_type = None):
        prop_list = set()
        for p in orig_prop_list:
            #print (p)
            if type(p) is tuple:
                prop = ' '.join([str(i).lower() for i in p])
            else:
                prop = ' '.join([str(i).lower() for i in p.predicate])
            #print ("prop",prop)
            if para_type:
                pred_parts = prop.split(' ')
                if pred_parts[0] not in self.predicate_type_map:
                    self.predicate_type_map[pred_parts[0]] = [para_type[p] for p in pred_parts[1:]]
            prop_list.add(prop)
        return prop_list

    def convert_domain_obj_map(self, prob_object):

        dom_map = {}
        for act in (prob_object.operators()):
            sorted_var_name = list(prob_object.domain.operators[act].variable_list.keys())
            sorted_var_name.sort()
            para_list = [ k + " - " + prob_object.domain.operators[act].variable_list[k] for k in sorted_var_name]
            par_map = {}
            for k in sorted_var_name:
                par_map[k] = prob_object.domain.operators[act].variable_list[k]
            action_name = act
            dom_map[action_name] = {}
            dom_map[action_name]['parameters'] = "@".join(para_list)
            dom_map[action_name]['precondition_pos'] = self.convert_prop_tuple_list(prob_object.domain.operators[act].precondition_pos, par_map)
            dom_map[action_name]['precondition_neg'] = self.convert_prop_tuple_list(prob_object.domain.operators[act].precondition_neg, par_map)
            dom_map[action_name]['effect_pos'] = self.convert_prop_tuple_list(prob_object.domain.operators[act].effect_pos, par_map)
            dom_map[action_name]['effect_neg'] = self.convert_prop_tuple_list(prob_object.domain.operators[act].effect_neg, par_map)


            dom_map[action_name]['precondition_pos'].add(ENFORCE_ORDERING_PRED)

        dom_map['problem'] = {}
        dom_map['problem']['init'] = copy.deepcopy(self.orig_start)
        dom_map['problem']['init'].add(ENFORCE_ORDERING_PRED)
        dom_map['problem']['goal'] = copy.deepcopy(self.goal_state)
        dom_map['current_cost'] = 0
        return dom_map

    def ground_all_operators(self, prob_object):
        ground_operators = []
        for act in prob_object.operators():
            ground_operators += list(prob_object.ground_operator(act))
        return ground_operators

    def generate_lattice_from_file(self):
        with open(self.lattice_file, 'r') as l_fd:
            lattice_map = yaml.load(l_fd)
        self.node_list = {}
        self.node_list[lattice_map['Lattice']['Init']] = copy.deepcopy(self.orig_dom_map)
        self.init_node = lattice_map['Lattice']['Init']
        self.edges = {}
        self.inverse_edges = {}
        while len(self.node_list.keys()) < len(lattice_map['Lattice']['Nodes']) + 1:
            for e_raw in lattice_map['Lattice']['Edges']:
                e = [i.lower() for i in e_raw]
                if e[0] in self.node_list.keys() and e[2] not in self.node_list.keys():
                    tmp_copy = copy.deepcopy(self.node_list[e[0]])
                    # Just a stand in for cases with no conditional effects
                    cost_delta = 0
                    for t in tmp_copy.keys():
                        if t != "current_cost" :
                            for k in tmp_copy[t].keys():
                                for p in self.node_list[e[0]][t][k]:
                                    if e[1] == p.split(' ')[0].lower():
                                        tmp_copy[t][k].remove(p)
                                        cost_delta += 1
                    if e[1] not in self.concret_costs.keys():
                        self.concret_costs[e[1]] = cost_delta

                    #print ("tmp_copy",e[1],tmp_copy['problem']['init'])
                    #print ("tmp_copy",e[1],tmp_copy['problem']['goal'])
                    tmp_copy['current_cost'] += cost_delta
                    self.node_list[e[2]] = tmp_copy
        
                if e[0] not in self.edges.keys():
                    self.edges[e[0]] = {} 
                    self.edges[e[0]][e[1]] = e[2] 
                else:
                    #self.edges[e[0]].append((e[1], e[2]))
                    self.edges[e[0]][e[1]] = e[2]
                    #self.inverse_edges[e[2]].append((e[1], e[0]))
                if e[2] not in self.inverse_edges.keys():
                    self.inverse_edges[e[2]] = {}
                    self.inverse_edges[e[2]][e[1]] = e[0]#[(e[1], e[0])]
                else:
                    self.inverse_edges[e[2]][e[1]] = e[0]#[(e[1], e[0])]

    def find_most_abstract_models(self, model):
        if model not in self.edges.keys():
            if self.all_foils_successful(model):
                print ("model",model)
                self.resolved_models[model] = [model]
                return [model]
            else:
                #print ("model",model)
                self.resolved_models[model] = []
                return []
        else:          
            curr_results = []
            for k in self.edges[model].keys():
                if k not in self.resolved_models.keys():
#                    res_models, abs_models = self.find_most_abstract_models(self.edges[model][k])
#                    resolved_models += res_models
#                    curr_results += abs_models
                    curr_results += self.find_most_abstract_models(self.edges[model][k])
                    self.resolved_models[k] = curr_results
            return curr_results

    def find_start_state(self):
        # also include checks for other restrictions
        self.start_state_belief_space = set(self.find_most_abstract_models(self.init_node))

    def make_problem_domain_file(self, curr_model, dom_file, prob_file):
        action_strings = []
        for act in  self.node_list[curr_model].keys():
            if act != "problem" and act !="current_cost":
                precondition_list = ['('+i+')' for i in self.node_list[curr_model][act]['precondition_pos']]
                precondition_list += ['(not ('+i+'))' for i in self.node_list[curr_model][act]['precondition_neg']]
                effect_list = ['('+i+')' for i in self.node_list[curr_model][act]['effect_pos']]
                effect_list += ['(not ('+i+'))' for i in self.node_list[curr_model][act]['effect_neg']]
                action_strings.append(ACTION_DEF_STR.format(act, " ".join(self.node_list[curr_model][act]['parameters'].split('@')),"\n".join(precondition_list),"\n".join(effect_list)))
        dom_str = self.domain_template_str.format("("+ENFORCE_ORDERING_PRED+")","\n".join(action_strings))

        goal_state_str_list = ['('+i+')' for i in  self.node_list[curr_model]['problem']['goal']]
        init_state_str_list = ['('+i+')' for i in self.node_list[curr_model]['problem']['init']]
        prob_str = self.prob_template_str.format("\n".join(init_state_str_list), "\n".join(goal_state_str_list))
        
        with open(dom_file, 'w') as d_fd:
            d_fd.write(dom_str)

        with open(prob_file, 'w') as p_fd:
            p_fd.write(prob_str)



    def create_action_copies_for_star(self, action_set, curr_state_id, next_state_id):
        act_map = {}
        # make an empty action
        action_name = "empty_action_"+str(curr_state_id)
        act_map[action_name] = {}
        act_map[action_name]['parameters'] = ""
        act_map[action_name]['precondition_pos'] = set()
        act_map[action_name]['precondition_pos'].add(AUT_STATE_PROP+str(curr_state_id))
        act_map[action_name]['precondition_neg'] = set()
        act_map[action_name]['effect_pos'] = set()
        act_map[action_name]['effect_pos'].add(AUT_STATE_PROP+str(next_state_id))
        act_map[action_name]['effect_neg'] = set()
        act_map[action_name]['effect_neg'].add(AUT_STATE_PROP+str(curr_state_id))


        # Make a copy of all actions curr_state that produces next_state_id
        for i in range(len(action_set)):
            act_name, act_defn = copy.deepcopy(action_set[i])
            act_defn["precondition_pos"].add(AUT_STATE_PROP+str(curr_state_id))
            act_defn["effect_neg"].add(AUT_STATE_PROP+str(curr_state_id))
            act_defn["effect_pos"].add(AUT_STATE_PROP+str(next_state_id))
            current_action_name = act_name+"_"+str(curr_state_id)+"_v1"
            act_map[current_action_name] = act_defn

        # Make a copy with curr_state that produces continue
        for i in range(len(action_set)):
            act_name, act_defn = copy.deepcopy(action_set[i])
            act_defn["precondition_pos"].add(AUT_STATE_PROP+str(curr_state_id))
            act_defn["effect_neg"].add(AUT_STATE_PROP+str(curr_state_id))
            act_defn["effect_pos"].add(AUT_STATE_PROP+str(curr_state_id)+"_continue")
            current_action_name = act_name+"_"+str(curr_state_id)+"_v2"
            act_map[current_action_name] = act_defn

        # Make a copy with continue that produces continue
        for i in range(len(action_set)):
            act_name, act_defn = copy.deepcopy(action_set[i])
            act_defn["precondition_pos"].add(AUT_STATE_PROP+str(curr_state_id)+"_continue")
            current_action_name = act_name+"_"+str(next_state_id)+"_v3"
            act_map[current_action_name] = act_defn

        # Make a copy with continue that produces next_state_id
        for i in range(len(action_set)):
            act_name, act_defn = copy.deepcopy(action_set[i])
            act_defn["precondition_pos"].add(AUT_STATE_PROP+str(curr_state_id)+"_continue")
            act_defn["effect_neg"].add(AUT_STATE_PROP+str(curr_state_id)+"_continue")
            act_defn["effect_pos"].add(AUT_STATE_PROP+str(next_state_id))
            current_action_name = act_name+"_"+str(curr_state_id)+"_v4"
            act_map[current_action_name] = act_defn
        return act_map

    def create_action_set_for_any(self, node, curr_model, spec_key = None, spec_type = None):
        act_map = {}
        node_type = list(node.succ_map)[0]
        next_node = node.succ_map[node_type]
        REPEAT_FLAG = False
        if node_type[-1] == '*':
            actual_node_type = node_type[:-1]
            REPEAT_FLAG = True
        else:
            actual_node_type = node_type

        node_parts = actual_node_type.split('_')
        current_actions = []

        for act in self.node_list[curr_model].keys():
            if act != "problem" and act != "current_cost":
                current_actions.append((act, copy.deepcopy(self.node_list[curr_model][act])))
        if not REPEAT_FLAG:
            act_map = {}
            for i in range(len(current_actions)):
                act_name, act_defn = current_actions[i]
                act_map[act_name+"_"+str(node.curr_id)] = act_defn
                act_map[act_name+"_"+str(node.curr_id)]["precondition_pos"].add(AUT_STATE_PROP+str(node.curr_id))
                act_map[act_name+"_"+str(node.curr_id)]["effect_neg"].add(AUT_STATE_PROP+str(node.curr_id))
                act_map[act_name+"_"+str(node.curr_id)]["effect_pos"].add(AUT_STATE_PROP+str(next_node.curr_id)) 
        else:
            act_map = self.create_action_copies_for_star(current_actions,node.curr_id,next_node.curr_id)

        return act_map, next_node



    def create_action_set_for_choice(self, node, curr_model, spec_key = None, spec_type = None):
        # Make one action for each choice
        action_map = {}
        node_type = list(node.succ_map)[0]
        next_node = node.succ_map[node_type]
        choice_actions = node_type.replace(')','').replace('ND(','').split('|')

        for act in choice_actions:
            node_parts = act.split('_')
            current_action = self.node_list[curr_model][node_parts[0]]
        
            para_list = current_action["parameters"].split("@")
            index = 0
            for arg in node_parts[1:]:
                para_parts = para_list[index].split(' - ')
                current_action["precondition_pos"].add(para_parts[0]+" = "+ arg)
                index += 1
            current_action["precondition_pos"].add(AUT_STATE_PROP+str(node.curr_id))
            current_action["effect_neg"].add(AUT_STATE_PROP+str(node.curr_id))
            current_action["effect_pos"].add(AUT_STATE_PROP+str(next_node.curr_id))
            current_action_name = node_type+"_"+str(node.curr_id)
            act_map[current_action_name] = current_action
        return act_map, next_node


    def create_actions_for_while(self, node, curr_model, spec_key = None, spec_type = None):
        # Make a test condition succ
        action_map = {}

        next_state_link = list(node.succ_map.keys())[0]
        test_conditions = next_state_link.split('WHILEtest@')[-1].split(',')
        while_start_node = node.succ_map[next_state_link]
        next_keys = list(while_start_node.succ_map)
        if WHILE_COND_SUCC in next_keys[0]:
            fail_link = next_keys[1]
            succ_link = next_keys[0]
        else:
            fail_link = next_keys[0]
            succ_link = next_keys[1]

        start_aut_state_pred = AUT_STATE_PROP+str(node.curr_id)

        print ("succ_link",succ_link,while_start_node.succ_map[succ_link].curr_id)
        print ("fail_link",fail_link,while_start_node.succ_map[fail_link].curr_id)
        # test success

        action_name = "test_condition_succ_for_while_"+str(node.curr_id)
        action_map[action_name] = {}
        action_map[action_name]['parameters'] = " "
        action_map[action_name]['precondition_pos'] = set()
        action_map[action_name]['precondition_pos'].add(start_aut_state_pred)

        for pred in test_conditions:
            action_map[action_name]['precondition_pos'].add(' '.join(pred.split('_')))
        
        action_map[action_name]['precondition_neg'] = set()
        action_map[action_name]['effect_pos'] = set()
        action_map[action_name]['effect_pos'].add(AUT_STATE_PROP+str(while_start_node.curr_id))
        action_map[action_name]['effect_neg'] = set()
        action_map[action_name]['effect_neg'].add(start_aut_state_pred)

        # Make a test condition fail
        action_name = "test_condition_fail_for_while_"+str(node.curr_id)
        action_map[action_name] = {}
        action_map[action_name]['parameters'] = " "
        action_map[action_name]['precondition_pos'] = set()
        action_map[action_name]['precondition_pos'].add(start_aut_state_pred)
        action_map[action_name]['precondition_neg'] = set()
        action_map[action_name]['precondition_neg_disj'] = set()

        # TODO: check if FD support disj negative precondition , if not split to different actions
        for pred in test_conditions:
            action_map[action_name]['precondition_neg_disj'].add(' '.join(pred.split('_')))

        action_map[action_name]['effect_pos'] = set()
        action_map[action_name]['effect_pos'].add(AUT_STATE_PROP+str(while_start_node.succ_map[fail_link].curr_id))
        action_map[action_name]['effect_neg'] = set()
        action_map[action_name]['effect_neg'].add(start_aut_state_pred)


        # TODO: I think this can be optimized by moving to a procedure
        # Add checks for succ actions
        curr_node = while_start_node#.succ_map[succ_link]
        orig_node_type = succ_link.split('@')[-1]#list(curr_node.succ_map)[0]
        node_type = orig_node_type
        curr_key = succ_link
        new_actions = {}
        while node_type != WHILE_END: 
            print ("node_type before",node_type)
            if WHILE_TEST_PREFIX in node_type:
                new_actions, curr_node = self.create_actions_for_while(curr_node, curr_model, spec_key = curr_key, spec_type = orig_node_type)
            elif IF_TEST_PREFIX in node_type:
                new_actions, curr_node = self.create_actions_for_if(curr_node, curr_model, spec_key = curr_key, spec_type = orig_node_type)
            elif ANY_PREFIX in node_type:
                new_actions, curr_node = self.create_action_set_for_any(curr_node, curr_model, spec_key = curr_key, spec_type = orig_node_type)
            elif ND_CHOICE in node_type:
                new_actions, curr_node = self.create_action_set_for_choice(curr_node, curr_model, spec_key = curr_key, spec_type = orig_node_type)
            else:
                new_actions, curr_node = self.create_actions_for_specific(curr_node, curr_model, spec_key = curr_key, spec_type = orig_node_type)
            for act in new_actions:
                action_map[act] = new_actions[act]
            orig_node_type = None
            curr_key = None
            node_type = list(curr_node.succ_map)[0]
            print ("node_type",node_type)
            print ("curr_node",curr_node.curr_id)

        new_actions, curr_node = self.create_actions_for_specific(curr_node, curr_model, spec_key = curr_key, spec_type = orig_node_type)
        for act in new_actions:
                action_map[act] = new_actions[act]

        return (action_map,while_start_node.succ_map[fail_link])




    def create_actions_for_if(self, node, curr_model, spec_key = None, spec_type = None):
        # Make a test condition succ IF
        # Make a test condition faile for Else
        action_map = {}

        next_state_link = list(node.succ_map.keys())[0]
        test_conditions = next_state_link.split('IFtest@')[-1].split(',')
        if_start_node = node.succ_node[next_state_link]
        next_keys = list(while_start_node.succ_map)
        if IF_COND_SUCC in next_keys[0]:
            fail_link = next_keys[1]
            succ_link = next_keys[0]
        else:
            fail_link = next_keys[0]
            succ_link = next_keys[1]

        start_aut_state_pred = AUT_STATE_PROP+str(node.curr_id)


        # test success

        action_name = "test_condition_succ_for_if_"+str(node.curr_id)
        action_map[action_name] = {}
        action_map[action_name]['parameters'] = " "
        action_map[action_name]['precondition_pos'] = set()
        action_map[action_name]['precondition_pos'].add(start_aut_state_pred)

        for pred in test_conditions:
            action_map[action_name]['precondition_pos'].add(' '.join(pred.split('_')))
        
        action_map[action_name]['precondition_neg'] = set()
        action_map[action_name]['effect_pos'] = set()
        action_map[action_name]['effect_pos'].add(AUT_STATE_PROP+str(if_start_node.succ_map[succ_link]))
        action_map[action_name]['effect_neg'] = set()
        action_map[action_name]['effect_neg'].add(start_aut_state_pred)

        # Make a test condition fail
        action_name = "test_condition_fail_for_if_"+str(node.curr_id)
        action_map[action_name] = {}
        action_map[action_name]['parameters'] = " "
        action_map[action_name]['precondition_pos'] = set()
        action_map[action_name]['precondition_pos'].add(start_aut_state_pred)
        action_map[action_name]['precondition_neg'] = set()
        action_map[action_name]['precondition_neg_disj'] = set()

        # TODO: check if FD support disj negative precondition , if not split to different actions
        for pred in test_conditions:
            action_map[action_name]['precondition_neg_disj'].add(' '.join(pred.split('_')))

        action_map[action_name]['effect_pos'] = set(AUT_STATE_PROP+str(if_start_node.succ_map[fail_link]))
        action_map[action_name]['effect_neg'] = set(start_aut_state_pred)


        # TODO: I think this can be optimized by moving to a procedure
        # Add checks for succ actions
        curr_node = if_start_node.succ_map[succ_link]
        node_type = list(curr_node.succ_map)[0]
        new_actions = {}
        
        if WHILE_TEST_PREFIX in node_type:
            new_actions, curr_node = self.create_actions_for_while(curr_node, curr_model)
        elif IF_TEST_PREFIX in node_type:
            new_actions, curr_node = self.create_actions_for_if(curr_node, curr_model)
        elif ANY_PREFIX in node_type:
            new_actions, curr_node = self.create_action_set_for_any(curr_node, curr_model)
        elif ND_CHOICE in node_type:
            new_actions, curr_node = self.create_action_set_for_choice(curr_node, curr_model)
        else:
            new_actions, curr_node = self.create_actions_for_specific(curr_node, curr_model)
        for act in new_actions:
            action_map[act] = new_actions[act]

        curr_node = if_start_node.succ_map[fail_link]
        node_type = list(curr_node.succ_map)[0]
        new_actions = {}
        
        if WHILE_TEST_PREFIX in node_type:
            new_actions, curr_node = self.create_actions_for_while(curr_node, curr_model)
        elif IF_TEST_PREFIX in node_type:
            new_actions, curr_node = self.create_actions_for_if(curr_node, curr_model)
        elif ANY_PREFIX in node_type:
            new_actions, curr_node = self.create_action_set_for_any(curr_node, curr_model)
        elif ND_CHOICE in node_type:
            new_actions, curr_node = self.create_action_set_for_choice(curr_node, curr_model)
        else:
            new_actions, curr_node = self.create_actions_for_specific(curr_node, curr_model)
        for act in new_actions:
            action_map[act] = new_actions[act]



        return (action_map,curr_node.succ_map[END_IF])




    def create_actions_for_specific(self, node, curr_model, spec_key = None, spec_type = None):
        # IF next state is end of while or if just return
        act_map = {}
        if not spec_key:
            node_type = list(node.succ_map)[0]
            next_node = node.succ_map[node_type]
        else:
            node_type = spec_type
            next_node = node.succ_map[spec_key]
        if node_type == END_IF or node_type == WHILE_END:
            # Add a dummy action that takes the current id and gives next id
            action_name = node_type+str(node.curr_id)
            act_map[action_name] = {}
            act_map[action_name]['parameters'] = ""
            act_map[action_name]['precondition_pos'] = set()
            act_map[action_name]['precondition_pos'].add(AUT_STATE_PROP+str(node.curr_id))
            act_map[action_name]['precondition_neg'] = set()
            act_map[action_name]['effect_pos'] = set()
            act_map[action_name]['effect_pos'].add(AUT_STATE_PROP+str(next_node.curr_id))
            act_map[action_name]['effect_neg'] = set()
            act_map[action_name]['effect_neg'].add(AUT_STATE_PROP+str(node.curr_id))

            return (act_map, node_type)
        REPEAT_FLAG = False
        if node_type[-1] == '*':
            actual_node_type = node_type[:-1]
            REPEAT_FLAG = True
        else:
            actual_node_type = node_type
        node_parts = actual_node_type.split('_')
        current_action = copy.deepcopy(self.node_list[curr_model][node_parts[0]])
        
        para_list = current_action["parameters"].split("@")
        index = 0
        for arg in node_parts[1:]:
            para_parts = para_list[index].split(' - ')
            current_action["precondition_pos"].add(para_parts[0]+" = "+ arg)
            index += 1
        if not REPEAT_FLAG:
            current_action["precondition_pos"].add(AUT_STATE_PROP+str(node.curr_id))
            current_action["effect_neg"].add(AUT_STATE_PROP+str(node.curr_id))
            current_action["effect_pos"].add(AUT_STATE_PROP+str(next_node.curr_id))
            current_action_name = node_type+"_"+str(node.curr_id)
            act_map[current_action_name] = current_action
        else:
            act_map = self.create_action_copies_for_star([(node_type,current_action)],node.curr_id,next_node.curr_id, curr_model)
        return act_map, next_node

    def make_compiled_problem_domain_file(self, curr_model, dom_file, prob_file, foil_obj):
        """
        TODO:
            Foils need to be , partially ordered with possible direct descendents
        """


        state_objs = set()
        new_predicates = set()

        for i in range(foil_obj.curr_highest_id):
            new_predicates.add('('+AUT_STATE_PROP+str(i)+')')
            new_predicates.add('('+AUT_STATE_PROP+str(i)+"_continue"+')')

        new_predicates.add('('+ENFORCE_ORDERING_PRED+')')
        current_action_map = {}

        curr_node = foil_obj.init_node

        CURRENTLY_IN_IF_BLOCK = False
        CURRENTLY_IN_WHILE = False
        
        PARSING_FOIL = True
        
        while len(curr_node.succ_map.keys()) > 0:
            node_type = list(curr_node.succ_map)[0]
            new_actions = {}
            # check if while
            if WHILE_TEST_PREFIX in node_type:
                new_actions, curr_node = self.create_actions_for_while(curr_node, curr_model)
            elif IF_TEST_PREFIX in node_type:
                new_actions, curr_node = self.create_actions_for_if(curr_node, curr_model)
            elif ANY_PREFIX in node_type:
                new_actions, curr_node = self.create_action_set_for_any(curr_node, curr_model)
            elif ND_CHOICE in node_type:
                new_actions, curr_node = self.create_action_set_for_choice(curr_node, curr_model)
            else:
                new_actions, curr_node = self.create_actions_for_specific(curr_node, curr_model)
            for act in new_actions:
                current_action_map[act] = new_actions[act]


        action_strings = []
        for act in  current_action_map:
            precondition_list = ['('+i+')' for i in current_action_map[act]['precondition_pos']]
            precondition_list += ['(not ('+i+'))' for i in current_action_map[act]['precondition_neg']]
            if 'precondition_neg_disj' in current_action_map[act]:
                disj_precs = ['(not ('+i+'))' for i in current_action_map[act]['precondition_neg_disj']]
                if len(current_action_map[act]) > 0:
                    precondition_list += ['(OR ' + " ".join(disj_precs)+')' ]
                else:
                    precondition_list += disj_precs

            effect_list = ['('+i+')' for i in current_action_map[act]['effect_pos']]
            effect_list += ['(not ('+i+'))' for i in current_action_map[act]['effect_neg']]
            action_strings.append(ACTION_DEF_STR.format(act, " ".join(current_action_map[act]['parameters'].split('@')),"\n".join(precondition_list),"\n".join(effect_list)))


        

        # Add check obs action
        # TODO: Assume that there are no duplicate objects

        goal_list = ['('+g+')' for g in self.node_list[curr_model]['problem']['goal']] 
        goal_list.append('('+AUT_STATE_PROP+str(curr_node.curr_id)+')')


        dom_str = self.domain_template_str.format("\n".join(new_predicates),"\n".join(action_strings))

        init_state_str_list = ['('+i+')' for i in self.node_list[curr_model]['problem']['init']] + ['('+AUT_STATE_PROP+'0)']
        prob_str = self.prob_template_str.format("\n".join(init_state_str_list), "\n".join(goal_list))
        
        with open(dom_file, 'w') as d_fd:
            d_fd.write(dom_str)

        with open(prob_file, 'w') as p_fd:
            p_fd.write(prob_str)



    def return_compiled_problem_domain_(self, curr_model, foil_obj):
        """
        TODO:
            Foils need to be , partially ordered with possible direct descendents
        """


        state_objs = set()
        new_predicates = set()

        for i in range(foil_obj.curr_highest_id):
            new_predicates.add('('+AUT_STATE_PROP+str(i)+')')
            new_predicates.add('('+AUT_STATE_PROP+str(i)+"_continue"+')')

        new_predicates.add('('+ENFORCE_ORDERING_PRED+')')
        current_action_map = {}

        curr_node = foil_obj.init_node

        CURRENTLY_IN_IF_BLOCK = False
        CURRENTLY_IN_WHILE = False
        
        PARSING_FOIL = True
        
        while len(curr_node.succ_map.keys()) > 0:
            node_type = list(curr_node.succ_map)[0]
            new_actions = {}
            # check if while
            if WHILE_TEST_PREFIX in node_type:
                new_actions, curr_node = self.create_actions_for_while(curr_node, curr_model)
            elif IF_TEST_PREFIX in node_type:
                new_actions, curr_node = self.create_actions_for_if(curr_node, curr_model)
            elif ANY_PREFIX in node_type:
                new_actions, curr_node = self.create_action_set_for_any(curr_node, curr_model)
            elif ND_CHOICE in node_type:
                new_actions, curr_node = self.create_action_set_for_choice(curr_node, curr_model)
            else:
                new_actions, curr_node = self.create_actions_for_specific(curr_node, curr_model)
            for act in new_actions:
                current_action_map[act] = new_actions[act]

        goal_list = ['('+g+')' for g in self.node_list[curr_model]['problem']['goal']]
        goal_list.append('('+AUT_STATE_PROP+str(curr_node.curr_id)+')')



        init_state_str_list = ['('+i+')' for i in self.node_list[curr_model]['problem']['init']] + ['('+AUT_STATE_PROP+'0)']

        return (current_action_map,goal_list,init_state_str_list,new_predicates)




    def all_foils_successful(self, curr_model):
        # return true if goal is empty here
        #if len(self.node_list[curr_model]['problem']['goal'][0]) == 0:
        #    return True
        prob_file = "/tmp/prob.pddl"
        dom_file = "/tmp/dom.pddl"
        plan_file = "/tmp/plan.sol"
        output_flag = True
        for i in range(len(self.foil)):
            self.make_compiled_problem_domain_file(curr_model, dom_file, prob_file, self.foil[i])
            print (PLANNER_COMMAND.format(dom_file, prob_file))
            #exit(0)
            output = [i.strip() for i in os.popen(PLANNER_COMMAND.format(dom_file, prob_file)).read().strip().split('\n')]
            if output == ['']:
                output = []
            print ("output",output,len(output))
            if len(output) == 0:
                return False
        return True

    def all_foils_resolved(self, curr_model):
        # return true if goal is empty here
        #if len(self.node_list[curr_model]['problem']['goal'][0]) == 0:
        #    return True
        prob_file = "/tmp/prob.pddl"
        dom_file = "/tmp/dom.pddl"
        plan_file = "/tmp/plan.sol"
        output_flag = True
        for i in range(len(self.foil)):
            self.make_compiled_problem_domain_file(curr_model, dom_file, prob_file, self.foil[i])
            output = [i.strip() for i in os.popen(PLANNER_COMMAND.format(dom_file, prob_file)).read().strip().split('\n')]
            if  len(output) > 0:
                return False
        return True

    def find_unresolved_foils(self, curr_model, current_foils):
        unreslv_foils = set()
        # return true if goal is empty here
        #if len(self.node_list[curr_model]['problem']['goal'][0]) == 0:
        #    return unreslv_foils
        prob_file = "/tmp/prob.pddl"
        dom_file = "/tmp/dom.pddl"
        plan_file = "/tmp/plan.sol"
        print ("current_foils:",current_foils)
        for f in current_foils:
            self.make_compiled_problem_domain_file(curr_model, dom_file, prob_file, f)
            output = [i.strip() for i in os.popen(PLANNER_COMMAND.format(dom_file, prob_file)).read().strip().split('\n')]

            if len(output[0]) > 0:
                unreslv_foils.add(copy.deepcopy(f))
        return unreslv_foils




    def run_blind_conformant(self):
        # Make a node for start state
        start_node = AbsNode(self, self.start_state_belief_space, [],  [i for i in self.foil])
        #exit(0)
        # Start search

        return astarSearch(start_node)


    def order_the_landmarks(self, parent_map, child_map):
        ordered_landmarks = [set()]
        for k in parent_map:
            if len(parent_map[k][GREEDY_NEC]) + len(parent_map[k][NAT_ORD]) == 0:
                ordered_landmarks[0].add(k)
        #print (ordered_landmarks)
        NOT_REACHED_END = True
        while NOT_REACHED_END:
            curr_layer = ordered_landmarks[-1]
            new_layer = set()
            for at in curr_layer:
                for ty in child_map[at]:
                    for ch in child_map[at][ty]:
                        new_layer.add(ch)
            if len(new_layer) > 0:
                ordered_landmarks.append(new_layer)
            else:
                NOT_REACHED_END = False
        return ordered_landmarks


    def make_compiled_problem_domain_file_for_landmark_exp(self, curr_model, dom_file, prob_file, landmark_parents, landmark_child):
        """
        TODO :
            currently ordered and single atom
            Also add the normal compilation 
        """

        #print (landmark_parents,landmark_child)
        #exit(0)

        ordered_landmarks = self.order_the_landmarks(landmark_parents, landmark_child)
        #print (ordered_landmarks)
        #exit(0)


        action_strings = []
        act_map, goal_list, init_list, new_predicates = self.return_compiled_problem_domain_(curr_model, self.foil[0])
        #obs 
        last_obs = None
        last_obs_pred = None
        #new_predicates = set()
        new_predicates.add(NEW_GOAL_PRED)
        new_predicates.add('('+ENFORCE_ORDERING_PRED+')')
        var_list = ['?a', '?b', '?c', '?d', '?e', '?f', '?g']

        act_ind = 0

        landmark_sets = set()
        landmark_preds = {}
        landmark_actions = {}
        greedy_necessary_preds = set()
        natural_preds = set()
        achieved_preds = set()
        landmar_first_time_test_preds = set()

        for landmark in landmark_parents:
            new_landmark_action_name = LANDMARK_OBS_ACT+landmark
            new_landmark_action_name = new_landmark_action_name.replace(' ','_')
            new_landmark_action = self.return_action_map_template()
            pars = landmark_parents[landmark]
            for par in pars[GREEDY_NEC]:
                gr_nc_par = LANDMARK_GREEDY_NEC+par
                gr_nc_par = gr_nc_par.replace(' ','_')
                new_landmark_action['precondition_pos'].add(gr_nc_par)
                greedy_necessary_preds.add('('+gr_nc_par+')')
            for par in pars[NAT_ORD]:
                nat_par = LANDMARK_NAT+par
                nat_par = nat_par.replace(' ','_')
                new_landmark_action['precondition_pos'].add(nat_par)
                natural_preds.add('('+nat_par+')')

            for lnd in landmark.split(LAND_CONJ_STR):
                new_landmark_action['precondition_pos'].add(lnd)
                lnd_pred = lnd.split(' ')[0]
                if lnd_pred not in landmark_preds:
                    landmark_preds[lnd_pred] = [lnd]
                else:
                    landmark_preds[lnd_pred].append(lnd)
                frst_pred = LANDMARK_FIRST_TIME+lnd
                frst_pred = frst_pred.replace(' ','_')
                new_landmark_action['precondition_pos'].add(frst_pred)
                landmar_first_time_test_preds.add('('+frst_pred+')')
            achv_lnd = LANDMARK_ACHIEVED+landmark
            achv_lnd = achv_lnd.replace(' ','_')
            new_landmark_action['effect_pos'].add(achv_lnd)

            if len(landmark_child[landmark][GREEDY_NEC]) > 0:
                gr_nc_par = LANDMARK_GREEDY_NEC+lnd
                gr_nc_par = gr_nc_par.replace(' ','_')
                new_landmark_action['effect_pos'].add(gr_nc_par)
                greedy_necessary_preds.add('('+gr_nc_par+')')
            if len(landmark_child[landmark][NAT_ORD])  > 0:
                nat_par = LANDMARK_NAT+lnd
                nat_par = nat_par.replace(' ','_')
                new_landmark_action['effect_pos'].add(nat_par)
                natural_preds.add('('+nat_par+')')
            achieved_preds.add('('+achv_lnd+')')
            landmark_actions[new_landmark_action_name] = new_landmark_action

            #if len(landmark_child[landmark][GREEDY_NEC]) + len(landmark_child[landmark][NAT_ORD]) == 0:
            landmark_sets.add(landmark)
            

        #exit(0)
        land_powerset = []

        max_cost = len(landmark_sets)

        for land in landmark_sets:
            land_powerset.append(land)
        #    for subs in itertools.combinations(landmark_sets,i+1):
        #        curr_set = set()
        #        for i in subs:
        #            curr_set.add(i)

        #        land_powerset.append(curr_set)

        new_predicates = new_predicates | natural_preds | achieved_preds | landmar_first_time_test_preds | greedy_necessary_preds
        #print (new_predicates)
        new_init_state = set()

        for act in  act_map:
            if act != "problem" and act !="current_cost":
                new_action = copy.deepcopy(act_map[act])
                for gr_nec in greedy_necessary_preds:
                    new_action['effect_neg'].add(gr_nec.replace('(','').replace(')',''))
                #found_landmark_preds = set()
                poss_landmark = {}
                for pred in new_action['effect_pos']:
                    pred_name = pred.split(' ')[0]
                    if pred_name in landmark_preds:
                        poss_landmark[pred] = []
                        for lands in landmark_preds[pred_name]:
                            poss_landmark[pred].append(lands)

                #print (poss_landmark)

                for k in poss_landmark:
                    for land in poss_landmark[k]:
                        if 'effect_cond_pos' not in new_action:
                            new_action['effect_cond_pos'] = set()
                        if 'effect_cond_neg' not in new_action:
                            new_action['effect_cond_neg'] = set()
                        new_eff = LANDMARK_NOTSET+land
                        new_eff = new_eff.replace('(','').replace(')','')
                        new_eff = new_eff.replace(' ','_')
                        eff_conds = [new_eff]
                        new_predicates.add('('+new_eff+')')
                        new_init_state.add('('+new_eff+')')

                        pred_arg_parts = k.split(' ')[1:]
                        land_arg_parts = []
                        for arg in land.split(' ')[1:]:
                            if arg != '':
                                land_arg_parts.append(arg)
                        try:
                            assert (len(pred_arg_parts) == len(land_arg_parts))
                        except:
                            print (pred_arg_parts)
                            print (land_arg_parts)
                            exit(1)

                        args_bindings = set()
                        for i in range(len(pred_arg_parts)):
                            args_bindings.add('= '+pred_arg_parts[i]+ ' ' + land_arg_parts[i])


                        frst = LANDMARK_FIRST_TIME+land
                        frst = frst.replace(' ','_')
                        new_action['effect_cond_pos'].add('#'.join(eff_conds + list(args_bindings))+'@'+ frst)
                        new_action['effect_cond_neg'].add('#'.join(eff_conds + list(args_bindings))+'@'+ new_eff)

                        new_action['effect_cond_neg'].add('#'.join(['not ('+new_eff+')']+ list(args_bindings))+'@'+ frst)

                landmark_actions[act] = new_action
        #print (new_init_state)
        #exit(0)

        for act in landmark_actions:
                precondition_list = ['('+i+')' for i in landmark_actions[act]['precondition_pos']]
                precondition_list += ['(not ('+i+'))' for i in landmark_actions[act]['precondition_neg']]
                effect_list = ['('+i+')' for i in landmark_actions[act]['effect_pos']]
                effect_list += ['(not ('+i+'))' for i in landmark_actions[act]['effect_neg']]
                if 'effect_cond_pos' in landmark_actions[act]:
                    for cond_eff in landmark_actions[act]['effect_cond_pos']:
                        #print (landmark_actions[act]['effect_cond_pos'])
                        cond, eff = cond_eff.split('@')
                        effect_list += ['(when (and '+' '.join(['('+i+')' for i in cond.split('#')])+') (and ('+eff+')))']

                action_strings.append(ACTION_DEF_STR.format(act, " ".join(landmark_actions[act]['parameters'].split('@')),"\n".join(precondition_list),"\n".join(effect_list)))

 

        # TODO: Assume that there are no duplicate objects
        

        #exit(0)

        for land_layer in ordered_landmarks:
            for land in land_layer:
                goal_act = {}
                land_achv = LANDMARK_ACHIEVED + land
                land_achv = land_achv.replace(' ','_')
                new_goal_action_name = LANDMARK_GOAL_CHECK
                goal_act[new_goal_action_name] = self.return_action_map_template()
                goal_act[new_goal_action_name]['precondition_pos'].add(achv_lnd)
                goal_act[new_goal_action_name]['effect_pos'] = set()
                goal_act[new_goal_action_name]['effect_pos'].add(NEW_GOAL_PRED.replace('(','').replace(')',''))
                new_action_stings = copy.deepcopy(action_strings)
                for act in goal_act:
                    precondition_list = ['('+i+')' for i in goal_act[act]['precondition_pos']]
                    precondition_list += ['(not ('+i+'))' for i in goal_act[act]['precondition_neg']]
                    effect_list = ['('+i+')' for i in goal_act[act]['effect_pos']]
                    effect_list += ['(not ('+i+'))' for i in goal_act[act]['effect_neg']]
                    if 'effect_cond_pos' in goal_act[act]:
                        for cond_eff in goal_act[act]['effect_cond_pos']:
                            #print (landmark_actions[act]['effect_cond_pos'])
                            cond, eff = cond_eff.split('@')
                            effect_list += ['(when (and '+' '.join(['('+i+')' for i in cond.split('#')])+') (and ('+eff+')))']

                    new_action_stings.append(ACTION_DEF_STR.format(act, " ".join(goal_act[act]['parameters'].split('@')),"\n".join(precondition_list),"\n".join(effect_list)))





                dom_str = self.domain_template_str.format("\n".join(new_predicates),"\n".join(new_action_stings))

                #init_state_str_list = ['('+i+')' for i in self.node_list[curr_model]['problem']['init']]
                prob_str = self.prob_template_str.format("\n".join(init_list + list(new_init_state)), " ".join([NEW_GOAL_PRED]))
        
                with open(dom_file, 'w') as d_fd:
                    d_fd.write(dom_str)

                with open(prob_file, 'w') as p_fd:
                    p_fd.write(prob_str)

                output = [i.strip() for i in os.popen(PLANNER_COMMAND.format(dom_file, prob_file)).read().strip().split('\n')]
                if output == ['']:
                    output = []
                if len(output) == 0:
                    return land
        return None





    def test_landmark_solvability(self,node, parent_map, child_map):
        test_status = False
        dom_file = "/tmp/lat_test_dom.pddl"
        prob_file = "/tmp/lat_test_prob.pddl"
        return self.make_compiled_problem_domain_file_for_landmark_exp(node, dom_file, prob_file, parent_map, child_map)
#        print ("Going to run the planner *******************")
#        output = [i.strip() for i in os.popen(PLANNER_COMMAND.format(dom_file, prob_file)).read().strip().split('\n')]
#        if output == ['']:
#            output = []
#        print ("landm plan",output)
        #if  len(output) > 0:
        #    return True
#        return output

    def check_reachable_for_landmark_list(self, node, parent_map, child_map, index):
        # TODO: Need to support empty landmarks
        #print ("landmark_list,",landmark_list)
        test_status = self.test_landmark_solvability(list(node.current_state)[0], parent_map, child_map)
        if len(test_status) > 0:
            return test_status
        return None


    def get_landmarks_in_last_node(self, node):
        landmark_list = []
        # TODO For now assume a single node is enough
        print ("inv",self.edges['c7'].keys(),list(node.current_state)[0],node.get_plan()[-1])
        last_node = self.edges[list(node.current_state)[0]][node.get_plan()[-1]]
        dom_file = "/tmp/lat_dom.pddl"
        prob_file = "/tmp/lat_prob.pddl"
        # TODO: Assuming a single wildcard foil
        self.make_compiled_problem_domain_file(last_node, dom_file, prob_file, self.foil[0])
        landmark_extraction_status = [i.strip() for i in os.popen(LAND_COMMAND.format(dom_file, prob_file)).read().strip().split('\n')]

        parent_map, child_map = parse_landmark_file('landmark.txt')
        #print ("ordered_landmarks",parent_map, child_map)
        filtered_landmark_parent_map = {}
        filtered_landmark_child_map = {}
        
        for p in parent_map:
            if AUT_STATE_PROP not in p:
                filtered_landmark_parent_map[p] = {'nat':set(), 'gn':set()}
                filtered_landmark_child_map[p] = {'nat':set(), 'gn':set()}
                for par_p in parent_map[p]['nat']:
                    if AUT_STATE_PROP not in par_p:
                        filtered_landmark_parent_map[p]['nat'].add(par_p)
                for chil_p in child_map[p]['nat']:
                    if AUT_STATE_PROP not in chil_p:
                        filtered_landmark_child_map[p]['nat'].add(chil_p)
                for par_p in parent_map[p]['gn']:
                    if AUT_STATE_PROP not in par_p:
                        filtered_landmark_parent_map[p]['gn'].add(par_p)
                for chil_p in child_map[p]['gn']:
                    if AUT_STATE_PROP not in chil_p:
                        filtered_landmark_child_map[p]['gn'].add(chil_p)


        #print ("filt",filtered_landmark_parent_map, filtered_landmark_child_map)

        # make sure all the goals are present
        #for g in node.problem.node_list[list(node.current_state)[0]]["problem"]["goal"]:
        #    if '('+g+')' not in filtered_landmark_list:
        #        print ("had to add the goal",g)
        #        filtered_landmark_list.append('('+g+')')


        #if len(filtered_landmark_list) <0:
        #    return None
        return (filtered_landmark_parent_map, filtered_landmark_child_map, node)

    def identify_landmarks_for_foil_actions_index(self, node, landmark_list):
        landmark_index = 0 #-1
        # TODO Assuming a single wildcard foil
        #first_acts = self.foil[0][0]
        #print ("first_acts",first_acts,self.node_list[list(node.current_state)[0]][first_acts.replace('(','').replace(')','').split(' ')[0]]['precondition_pos'])
        #for land_ind in range(len(landmark_list)):
        #    if landmark_index == -1:
        #        pred_name = landmark_list[land_ind].replace('(','').replace(')','').split(' ')[0]
        #        for act in first_acts.split('@'):
        #            precs = [i.split(' ')[0] for i in self.node_list[list(node.current_state)[0]][act.replace('(','').replace(')','').split(' ')[0]]['precondition_pos']]
        #            if pred_name in precs:
        #                landmark_index = land_ind
        return landmark_index


    def explain(self):
        self.find_start_state()
        print ("Starting state",self.start_state_belief_space)

        curr_node = self.run_blind_conformant()

        # find landmarks
        parent_map, child_map, land_node = self.get_landmarks_in_last_node(curr_node)
        relevant_landmark_index = 0 #self.identify_landmarks_for_foil_actions_index(land_node, parent_map, child_map)
        #print ("relevant_landmark_index",relevant_landmark_index,landmark_list[relevant_landmark_index])
        # Check if any relevant landmark is unreachable
        print ("Looking for landmark failures ################")
        failed_landmark = self.check_reachable_for_landmark_list(curr_node, parent_map, child_map, relevant_landmark_index)
        print ("failed landmark",failed_landmark)
        return (curr_node.get_plan(), failed_landmark)



