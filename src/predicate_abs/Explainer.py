import argparse
import sys
import time
from Problem import *

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
    parser.add_argument('-f', '--foil_file', type=str, help="foil Plan file prefix.", required=True)
    parser.add_argument('-n', '--foil_count', type=str, help="foil count.", required=True)
    parser.add_argument('-l', '--lattice_file', type=str, help="Lattice file (yaml).")
    parser.add_argument('-q', '--proposition_file', type=str, help="File with the list of proposition.")
    parser.add_argument('-r', '--domain_templ', type=str, help="Domain template file")
    parser.add_argument('-s', '--prob_templ', type=str, help="Problem template file")
    parser.add_argument('-t', '--search_type', type=str, help="Search type to be performed")


    if not sys.argv[1:] or '-h' in sys.argv[1:]:
        print (parser.print_help())
        sys.exit(1)
    args = parser.parse_args()
    

    problem = Problem(args.domain_model, args.problem, args.foil_file, args.foil_count, args.lattice_file, args.domain_templ, args.prob_templ, args.search_type)
    st_time = time.time()
    pl = problem.explain()
    cost = 0
#    for p in pl:
#        cost += problem.concret_costs[p]
    print ("Explanation",pl)
#    print ("Cost >>", cost)
    print ("Explanation Size >>>",len(pl))
    print ("Total time >>>",time.time() - st_time)

if __name__ == "__main__":
    main()
