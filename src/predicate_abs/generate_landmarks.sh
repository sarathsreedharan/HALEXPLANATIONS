#!/bin/bash 

#RADAR_REPO="/media/data_mount/mycode/RADAR/FD/src"
LANDMARK_FD_REPO="/media/data_mount/mycode/FD_EXPT_VERS/FD_LAND_DUMP"
dom_file=$1
prob_file=$2

rm landmark.txt 

python ${LANDMARK_FD_REPO}/fast-downward.py --build "release64"   $dom_file $prob_file  --search "astar(lmcount(lm_factory=lm_hm(m=1)))"|grep "LM " > landmark.txt

#python ${RADAR_REPO}/fast-downward.py $dom_file $prob_file  --landmarks name=lm_zg > /dev/null

#cat landmark.txt #|sed 's/,//'|sed 's/(/ /'|sed 's/^/(/'|sed 's/ )/)/' #|sed 's/.*Atom //'|sed 's/,//'|sed 's/(/ /'|sed 's/^/(/'|sed 's/ )/)/'


