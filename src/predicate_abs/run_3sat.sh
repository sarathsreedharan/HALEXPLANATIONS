#!/bin/bash
mkdir -p /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_3SAT_LOG/

for i in {1..25}; 
do (timeout 60m time python3 Explainer.py -d ../../domains/unsolv_test/3sat/domain${i}.pddl -p ../../domains/unsolv_test/3sat/prob${i}.pddl -f ../../domains/unsolv_test/3sat/foil -n 1 -l ../../domains/unsolv_test/3sat/lattice_2.yaml -r ../../domains/unsolv_test/3sat/domain${i}_templ.pddl -s ../../domains/unsolv_test/3sat/prob${i}_templ.pddl -t blind) > /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_3SAT_LOG/abs_log_${i} 2>&1; 
timeout 30m ./certify.sh /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/3sat/domain.pddl /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/3sat/prob${i}.pddl > /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_3SAT_LOG/orig_log_${i} 
done
