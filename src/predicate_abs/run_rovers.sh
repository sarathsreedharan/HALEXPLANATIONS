#!/bin/bash
mkdir -p /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_ROVERS_LOG/

for i in 1 #{1..20}; 
do 
#(timeout 30m 
time python3 Explainer.py -d ../../domains/unsolv_test/rovers/domain.pddl -p ../../domains/unsolv_test/rovers/prob${i}.pddl -f ../../domains/unsolv_test/rovers/foil -n 1 -l ../../domains/unsolv_test/rovers/lattice_8.yaml -r ../../domains/unsolv_test/rovers/domain_templ.pddl -s ../../domains/unsolv_test/rovers/prob${i}_templ.pddl -t blind #) > /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_ROVERS_LOG/abs_log_${i} 2>&1; 
#timeout 30m ./certify.sh /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/rovers/domain.pddl /media/data_mount/mycode/WILD_EXPLANATIONS/GROUNDED_DCK_FOILS_CERTIFY/domains/unsolv_test/rovers/prob${i}.pddl > /media/data_mount/mycode/PARTIALLY_SPECIFIED_WORKSPACE/INIT_CERT_TEST_ROVERS_LOG/orig_log_${i} 
done
