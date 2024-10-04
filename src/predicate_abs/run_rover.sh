#!/bin/bash
#mkdir -p /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_BOTTLE_LOG/

for i in 1 #{1..25}; 
do (time python3 Explainer.py -d ../../domains/rover/approx_scenario/domain.pddl -p ../../domains/rover/approx_scenario/prob.pddl -f ../../domains/rover/approx_scenario/foil -n 1 -l ../../domains/rover/approx_scenario/lattice_4.yaml -r ../../domains/rover/approx_scenario/domain_templ.pddl -s ../../domains/rover/approx_scenario/prob_templ.pddl -t blind) #> /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_BOTTLE_LOG/abs_log_${i} 2>&1; 
#./certify.sh /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/rover/approx_scenario/domain.pddl /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/rover/approx_scenario/prob${i}.pddl > /media/data_mount/mycode/WILD_EXPLANATIONS_WORKSPACE/INIT_CERT_TEST_BOTTLE_LOG/orig_log_${i} 
done
