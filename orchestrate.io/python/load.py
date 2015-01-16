#!/usr/bin/python
# -*- coding: utf-8 -*-

from porc import Client
import sys
import time

argvs = sys.argv
if len(argvs)>1:
    number_of_record = int(argvs[1])
    n = int(argvs[2])
else:
    number_of_record = 1000
    n = 100

f = open('../streetname.txt','r')
food = f.readlines()
f.close()
for i in xrange(len(food)):
    food[i] = food[i].strip()


YOUR_API_KEY = "ce17e2a6-eaa3-47a7-bd16-8a84a7535cf7"
client = Client(YOUR_API_KEY)
d = {}

starttime=time.time()
for i in xrange(0,number_of_record):
    for k in xrange (1,n):
        d.update({food[i+k]:food[i+10000+k]})
    response = client.put('acidtest', food[i], d)

print "Writing : " + str(number_of_record) + "records : " + str(n) + "cols : " + str(time.time()-starttime) + "sec"

starttime=time.time()
for i in xrange(0,number_of_record):
    response = client.get('acidtest', food[i])

print "Reading : " + str(number_of_record) + "records : " + str(n) + "cols : " + str(time.time()-starttime) + "sec"
