import os
import sys
import copy

def parse_land_line(line):
    PARSE_STR = "Atom "
    return line.split(PARSE_STR)[-1]

def parse_landmark_file(lfile):
    with open(lfile) as l_fd:
        land_content = [l.strip() for l in l_fd.readlines()]
    ind = 0
    parent_map = {}
    child_map = {}
    while ind < len(land_content):
        new_land = []
        curr_atom = parse_land_line(land_content[ind])
        if curr_atom not in parent_map:
            parent_map[curr_atom] = set()
            child_map[curr_atom] = set()
        ind += 1
        while ind < len(land_content) and ('<-' in land_content[ind] or '->' in land_content[ind]):
            if '<-' in land_content[ind]:
                parent_map[curr_atom].add(parse_land_line(land_content[ind]))
            else:
                child_map[curr_atom].add(parse_land_line(land_content[ind]))
            ind+=1

    #print (parent_map)
    #print (child_map)

    ordered_landmarks = [set()]
    for k in parent_map:
        if len(parent_map[k]) == 0:
            ordered_landmarks[0].add(k)

    NOT_REACHED_END = True

    while NOT_REACHED_END:
        curr_layer = ordered_landmarks[-1]
        new_layer = set()
        for at in curr_layer:
            for ch in child_map[at]:
                new_layer.add(ch)
        if len(new_layer) > 0:
            ordered_landmarks.append(new_layer)
        else:
            NOT_REACHED_END = False

    # print
    lid = 0
    for ly in ordered_landmarks:
        print ("Layer id = ", str(lid))
        print (ly)
        lid +=1




if __name__ == "__main__":
    parse_landmark_file('landmark.txt')
