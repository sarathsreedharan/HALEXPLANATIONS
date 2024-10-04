#!/bin/bash
pushd /media/data_mount/mycode/WILD_EXPLANATIONS/ICAPS_CERT/src/unsolvability > /dev/null
./run_forme $1 $2|grep -iE "size|time"|grep -i total
popd > /dev/null
