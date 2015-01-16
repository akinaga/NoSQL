#!/bin/bash

cat result/load.*.1.100.100.* > load.1.100.100.result
cat result/load.*.50.100.100.* > load.50.100.100.result
cat result/load.*.100.100.100.* > load.100.100.100.result

cat result/load.*.1.1000.100.* > load.1.1000.100.result
cat result/load.*.50.1000.100.* > load.50.1000.100.result
cat result/load.*.100.1000.100.* > load.100.1000.100.result
