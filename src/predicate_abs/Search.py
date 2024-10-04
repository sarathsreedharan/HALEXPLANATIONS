from queue import PriorityQueue, Queue
from functools import total_ordering
import copy
import time
import math
GAMMA = 0.01
class Node:
    def __init__(self):
        self.current_state = set()
        self.problem = None
        self.plan = []

    def get_state(self):
        return self.current_state

    def goal_test(self):
        pass

    def get_successors(self):
        pass

    def get_plan(self):
        return self.plan

    def get_heuristc(self):
        return 0

    def get_fvalue(self):
        return self.get_heuristc() + len(self.get_plan())

    def expand_operations(self):
        pass

@total_ordering
class AbsNode(Node):
    def __init__(self, problem, current_state, curr_plan=[], current_foils = [], cogn_bound = -1):
        self.current_state = set(current_state)
        self.current_foils = current_foils
        self.problem = problem
        self.plan = curr_plan
        self.cognitive_bound = cogn_bound
        self.current_cost = 0
        self.current_chunk = 0


    def goal_test(self):
        curr_flag = True
        #print ("self.current_state:",self.current_state)
        #print ("self.current_state:",self.problem.test_foil_condition_pos('c112'))
        #print ("self.current_state:",self.problem.test_foil_condition_neg('c112'))
        #exit(0)
        #print (self.current_foils)
        if len(self.current_foils) == 0: #and self.current_cost >= int(cb):
            return True
#        for model in self.current_state:
            #print ("model",model)
#            if not self.problem.test_foil_condition_pos(model):
#                curr_flag = False
#        return curr_flag

    def greedy_goal_test(self, cb):
        if len(self.current_foils) == 0: #and self.current_cost >= int(cb):
            return True


    def get_successors(self, cb = -1):
        possible_concret = set()
        successor_list = []
        for model in self.current_state:
            try:
                edge_list = self.problem.inverse_edges[model]
                for e in edge_list.keys():
                    possible_concret.add(e)
            except:
                pass
        for prop in possible_concret:
            tmp_succ = set()
            for model in self.current_state:
                try:
                    tmp_succ.add(self.problem.inverse_edges[model][prop])
                except:
                    tmp_succ.add(model)
            tmp_model = AbsNode(self.problem, tmp_succ, self.plan + [prop], self.current_foils)
            tmp_model.current_cost = self.current_cost + self.problem.concret_costs[prop]
                #tmp_set = set()
                #for m2 in tmp_model.current_state:
                #    tmp_set |= set(tmp_model.problem.find_unresolved_foils(m2,tmp_model.current_foils))
                #tmp_model.current_foils = copy.deepcopy(tmp_set)
            successor_list.append(tmp_model)
        return successor_list


    def get_fvalue(self):
        return self.get_heuristc() + self.current_cost

    def get_chunk_fvalue(self):
        return len(self.current_foils)

    def __eq__(self, other):
        return (list(self.current_state)[0]) == (list(other.current_state)[0])

    def __lt__(self, other):
        return (list(self.current_state)[0]) < (list(other.current_state)[0])

    def expand_operations(self):
        tmp_set = []
        for m in self.current_state:
            unres = self.problem.find_unresolved_foils(m,self.current_foils)
            print ("UNRES",unres,m)
            for p in unres:
                tmp_set.append(p)
        self.current_foils = copy.deepcopy(tmp_set)

@total_ordering
class LatNode(Node):
    def __init__(self, lattice, current_state, curr_plan=[]):
        self.current_state = current_state
        self.problem = lattice
        self.plan = curr_plan


    def goal_test(self):
        return self.problem.verify_the_lattice(self.current_state)
    

    def get_successors(self):
        return self.problem.get_all_successor_nodes(self) 

    def get_state(self):
        #print (str(self.current_state["edges"]))
        return str(self.current_state["edges"])

    def __eq__(self, other):
        return (list(self.current_state)[0]) == (list(other.current_state)[0])

    def __lt__(self, other):
        return (list(self.current_state)[0]) < (list(other.current_state)[0])





def astarSearch(start_state):
    fringe = PriorityQueue()
    closed = set()
    nodes_expanded = 0
    fringe.put((0,start_state))
    while not fringe.empty():
        print ("Search iteration")
        val, node = fringe.get()#[1]
        node.expand_operations()
        if node.goal_test():
            print ("In Astar Goal Found! Number of Nodes Expanded =", nodes_expanded, "foils",node.current_foils)
            return node #.get_plan()
        if frozenset(node.get_state()) not in closed:
            #print (closed)
            closed.add(frozenset(node.get_state()))
            successor_list = node.get_successors()
            nodes_expanded += 1

            if not nodes_expanded % 100:
                print ("Number of Nodes Expanded =", nodes_expanded)
            
            while successor_list: 
                candidate_node = successor_list.pop()
                #print (candidate_node.plan)
                fringe.put((candidate_node.get_fvalue(), candidate_node))

    return None

def BFSSearch(start_state):
    fringe = Queue()
    closed = set()
    nodes_expanded = 0
    fringe.put((0,start_state))

    while not fringe.empty():
        
        val, node = fringe.get()#[1]
        #print ("node vla",val)
        if node.goal_test():
            print ("In Blind, Goal Found! Number of Nodes Expanded =", nodes_expanded)
            return node #.get_plan()
        if node.get_state() not in closed:
            #print (closed)
            closed.add(node.get_state())
            successor_list = node.get_successors()
            nodes_expanded += 1
            print ("Number of Nodes Expanded =", nodes_expanded)
            
            while successor_list: 
                candidate_node = successor_list.pop()
                fringe.put((candidate_node.get_fvalue(), candidate_node))

    return None


def GreedySearch(start_state):
    closed = set()
    nodes_expanded = 0
    current_node = start_state
    #print (current_node.current_state)
    #for k in current_node.pred_foil_map.keys():
    #    print (k,len(current_node.pred_foil_map[k]))
    while current_node:
        if current_node.goal_test():
            print ("Goal Found! Number of Nodes Expanded =", nodes_expanded)
            return current_node #.get_plan()
        min_val = 1000000
        min_node = None
        successor_list = current_node.get_successors()
        while successor_list:
            candidate_node = successor_list.pop()
            inter_count = len(current_node.current_foils & current_node.pred_foil_map[candidate_node.plan[-1]])
            if inter_count > 0:
                val = float(current_node.problem.concret_costs[candidate_node.plan[-1]])/float(inter_count)
            else:
                val =  float(current_node.problem.concret_costs[candidate_node.plan[-1]]) * 100 # This is never the right choice to make in this setting
            if min_val > val:
                min_val = val
                min_node = copy.deepcopy(candidate_node)
        current_node = copy.deepcopy(min_node)
        new_foils = current_node.current_foils - current_node.pred_foil_map[current_node.plan[-1]]
        current_node.current_foils = copy.deepcopy(new_foils)
        print (current_node.plan)
    return None
