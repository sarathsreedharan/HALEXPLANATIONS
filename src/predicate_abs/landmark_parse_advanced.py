import os
import re
import sys
import copy

def parse_land_line(orig_line, relative = False):
    line = re.sub('^LM \d Atom','StAtom',orig_line)
    PARSE_STR = "Atom "
    CONJ_STR = "CONJ"
    if 'conj {Atom ' not in line:
        atom = line.split(PARSE_STR)[-1].split(' (')[0]
    else:
        atom_list = []
        for atm_strs in line.split(CONJ_STR)[-1].split(', Atom '):
            if PARSE_STR in atm_strs:
                atom_list.append(atm_strs.split(PARSE_STR)[-1].split(' (')[0])
            else:
                atom_list.append(atm_strs.split('conj {Atom ')[-1].split(' (')[0])
        atom = '&'.join(atom_list)
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

if __name__ == "__main__":
    parse_landmark_file('landmark.txt')
