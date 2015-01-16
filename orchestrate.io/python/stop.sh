#!/bin/bash -f

while :
do
        sleep 1
        echo $(ps | grep python | grep -v grep | wc -l)
        if [ $(ps | grep python | grep -v grep | wc -l) -eq 0 ]; then
                break
        fi
done
