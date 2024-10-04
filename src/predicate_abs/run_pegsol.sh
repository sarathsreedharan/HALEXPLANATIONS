#!/bin/bash
mkdir -p /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_PEGSOL_LOG/

for i in {1..20} 
do 
#(timeout 30m time python3 Explainer.py -d ../../domains/unsolv_test/pegsol/domain.pddl -p ../../domains/unsolv_test/pegsol/prob${i}.pddl -f ../../domains/unsolv_test/pegsol/foil -n 1 -l ../../domains/unsolv_test/pegsol/lattice_3.yaml -r ../../domains/unsolv_test/pegsol/domain_templ.pddl -s ../../domains/unsolv_test/pegsol/prob${i}_templ.pddl -t blind) > /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_PEGSOL_LOG/abs_log_${i} 2>&1; 


(timeout 30m time ./fdplan.sh ../../domains/unsolv_test/pegsol/domain.pddl ../../domains/unsolv_test/pegsol/prob${i}.pddl ) > /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_PEGSOL_LOG/orig_log_${i} 2>&1;
#timeout 30m ./certify.sh /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/pegsol/domain.pddl /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/pegsol/prob${i}.pddl > /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_PEGSOL_LOG/orig_log_${i} 
done
