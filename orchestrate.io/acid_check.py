#!/usr/bin/python
# -*- coding: utf-8 -*-

from porc import Client
import json
import codecs
import time
import random

f = open('streetname.txt','r')
food = f.readlines()
f.close()
for i in xrange(len(food)):
    food[i] = food[i].strip()

YOUR_API_KEY = "ce17e2a6-eaa3-47a7-bd16-8a84a7535cf7"
number_of_record = 1000

client = Client(YOUR_API_KEY)

print "***************** writing start ********************"
starttime=time.time()
for i in xrange(0,number_of_record):
    d = {food[i+100]:food[i+1000], food[i+200]:food[i+2000]}
    #json_data = json.dumps(d)
#   print d
    #print json_data
    response = client.put('acidtest', food[i], d)
#    response = client.get('acidtest', food[i])
#    print response.json
#    print "---------------"
    #response.raise_for_status()

print str(time.time()-starttime) + "sec"
print "***************** reading start ********************"
starttime=time.time()
for i in xrange(0,number_of_record):
#    d = {food[i+100]:food[i+1000], food[i+200]:food[i+2000]}
    #json_data = json.dumps(d)
#   print d
    #print json_data
#    response = client.put('acidtest', food[i], d)
    j = random.randint(0,number_of_record-1)
    response = client.get('acidtest', food[j])
#    print response.json
#    print "---------------"
    #response.raise_for_status()

print str(time.time()-starttime) + "sec"
print "***************** ACID verification start ********************"
starttime=time.time()
for i in xrange(0,number_of_record):
    d = {food[i+500]:food[i+5000], food[i+500]:food[i+6000]}
    #json_data = json.dumps(d)
#    print d
    #print json_data
    response = client.put('acidtest', food[i], d)
    response = client.get('acidtest', food[i])
#    print response.json
    if d!=response.json:
        print d
        print response.json
        print "unmatched"
    #print "---------------"
    #response.raise_for_status()
print str(time.time()-starttime) + "sec"

