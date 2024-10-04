import re


WHILE_KEYWORD = "while"
WHILE_START_KEYWORD = "do"
WHILE_STOP_KEYWORD = "done"

IF_KEYWORD = "if"
IF_START_KEYWORD = "then"
ELSE_KEYWORD = "else"
IF_STOP_KEYWORD = "fi"



class AutNode:
    def __init__(self, curr_id):
        self.curr_id = curr_id
        self.succ_map = {}




class DCKParser:
    def __init__(self, dck_file):
        self.init_node = AutNode(0)
        self.curr_highest_id = 1
        self.annotated_lines = []
        with open(dck_file) as d_fd:
            self.dck_script = [i.strip() for i in d_fd.readlines()]
        self.parse_dck_script()

    def add_a_child_node(self, old_node, line):
        new_node = AutNode(self.curr_highest_id)
        self.curr_highest_id += 1
        old_node.succ_map[line] = new_node

        return new_node


    def extract_while_loop(self, stripped_line, c_index, parent_node, LAST_STEP_LABEL=""):
        condition_tmp = re.sub("^\s*"+WHILE_KEYWORD+"\s*","", stripped_line)
        condition = re.sub(WHILE_KEYWORD+"\s*$","", condition_tmp)
        self.annotated_lines.append((LAST_STEP_LABEL+"WHILEtest@"+condition, self.curr_highest_id))
        curr_node = self.add_a_child_node(parent_node, LAST_STEP_LABEL+"WHILEtest@"+condition)
        initial_node = curr_node
        c_index += 1
        INSIDE_WHILE_LOOP = True
        LAST_STEP_LABEL ="WHILE_COND_SUCC@"
        while c_index < len(self.dck_script) and INSIDE_WHILE_LOOP:
            stripped_line_tmp = re.sub("^\s*","", self.dck_script[c_index])
            stripped_line = re.sub("\s*$","", stripped_line_tmp)
            #print (stripped_line)
            #exit(0)
            if WHILE_START_KEYWORD != stripped_line:
                if stripped_line == WHILE_STOP_KEYWORD:
                    #print ("here")
                    #exit(0)
                    INSIDE_WHILE_LOOP = False
                    c_index += 1
                else:
                    c_index, curr_node = self.parse_dck_statements(c_index, curr_node,LAST_STEP_LABEL)
                if LAST_STEP_LABEL != "":
                    LAST_STEP_LABEL = ""
            else:
                 c_index += 1

        curr_node.succ_map["END_OF_WHILE_LOOP"] = initial_node
        return c_index, initial_node


    def extract_if_condition(self, stripped_line, c_index, curr_node,LAST_STEP_LABEL=""):
        condition_tmp = re.sub(WHILE_KEYWORD+"^\s*","", stripped_line)
        condition = re.sub(WHILE_KEYWORD+"\s*$","", condition_tmp)
        self.annotated_lines.append(("IFtest@"+condition, self.curr_highest_id))
        curr_node = self.add_a_child_node(parent_node, "IFtest@"+condition)
        c_index += 1
        initial_node = curr_node
        INSIDE_IF_CONDITION = True
        LAST_STEP_LABEL = "IFBLOCK@"
        while c_index < len(self.dck_script) and INSIDE_IF_CONDITION:
            stripped_line_tmp = re.sub("^\s*","", self.dck_script[c_index])
            stripped_line = re.sub("\s*$","", stripped_line_tmp)
            if not stripped_line == IF_START_KEYWORD:
                if stripped_line == ELSE_KEYWORD:
                    INSIDE_IF_CONDITION = False
                    c_index += 1
                else:
                    c_index, curr_node = self.parse_dck_statements(c_index, curr_node,LAST_STEP_LABEL)
                if LAST_STEP_LABEL != "":
                    LAST_STEP_LABEL = ""
            else:
                c_index += 1

        last_if_statement_node = curr_node

        curr_node = initial_node
        INSIDE_ELSE_CONDITION = True

        LAST_STEP_LABEL = "ELSEBLOCK@"

        while c_index < len(self.dck_script) and INSIDE_ELSE_CONDITION:
            stripped_line_tmp = re.sub("^\s*","", self.dck_script[c_index])
            stripped_line = re.sub("\s*$","", stripped_line_tmp)
            if stripped_line == IF_STOP_KEYWORD:
                INSIDE_ELSE_CONDITION = False
                c_index += 1
            else:
                c_index, curr_node = self.parse_dck_statements(c_index, curr_node, LAST_STEP_LABEL)
            if LAST_STEP_LABEL != "":
                LAST_STEP_LABEL = ""
        
        end_condition_node = self.add_a_child_node(curr_node, "END_CONDITION")
        last_if_statement_node.succ_map["END_CONDITION"] = end_condition_node
        return c_index, end_condition_node

    def parse_dck_script(self):
        c_index = 0
        curr_node = self.init_node
#        print ("c_index",c_index,type(c_index))
        while c_index < len(self.dck_script):
            c_index, curr_node = self.parse_dck_statements(c_index, curr_node)
        
    def parse_dck_statements(self, c_index, curr_node, LAST_STEP_LABEL=""):
        stripped_line = re.sub("^\s*","", self.dck_script[c_index])
        if WHILE_KEYWORD in stripped_line:
            c_index, curr_node = self.extract_while_loop(stripped_line, c_index, curr_node,LAST_STEP_LABEL)
        elif IF_KEYWORD in stripped_line:
            c_index, curr_node = self.extract_if_condition(stripped_line, c_index, curr_node,LAST_STEP_LABEL)
        else:
            self.annotated_lines.append((LAST_STEP_LABEL+stripped_line, self.curr_highest_id))
            curr_node = self.add_a_child_node(curr_node, LAST_STEP_LABEL+stripped_line)
            c_index += 1
            LAST_STEP_LABEL=""
        return c_index, curr_node

if __name__ == '__main__':
    DC = DCKParser('test.dck')
