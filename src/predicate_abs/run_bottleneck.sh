#!/bin/bash
mkdir -p /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_BOTTLE_LOG/

for i in 1 #{1..25}; 
do (time python3 Explainer.py -d ../../domains/unsolv_test/bottleneck/domain.pddl -p ../../domains/unsolv_test/bottleneck/prob${i}.pddl -f ../../domains/unsolv_test/bottleneck/foil -n 1 -l ../../domains/unsolv_test/bottleneck/lattice_3.yaml -r ../../domains/unsolv_test/bottleneck/domain_templ.pddl -s ../../domains/unsolv_test/bottleneck/prob${i}_templ.pddl -t blind) > /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_BOTTLE_LOG/abs_log_${i} 2>&1; 
#./certify.sh /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/bottleneck/domain.pddl /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/bottleneck/prob${i}.pddl > /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_BOTTLE_LOG/orig_log_${i} 
done
