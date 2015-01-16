#!/bin/sh

bash load.sh 1 100 100
bash stop.sh
bash load.sh 50 100 100
bash stop.sh
bash load.sh 100 100 100
bash stop.sh

bash load.sh 1 1000 100
bash stop.sh
bash load.sh 50 1000 100
bash stop.sh
bash load.sh 100 1000 100
bash stop.sh
