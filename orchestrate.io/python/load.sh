#!/bin/bash -f

for i in $(seq 1 $1);
do
    echo $i
    python load.py $2 $3 > result/load.$i.$1.$2.$3.result &
done
