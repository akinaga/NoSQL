#!/bin/bash -f

for i in $(ps ax | grep python | cut -c1-5);
do
    kill -9 $i
done
