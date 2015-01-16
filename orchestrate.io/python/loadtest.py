#!/usr/bin/python
# -*- coding: utf-8 -*-

from porc import Client
import json
import codecs
import time
import random

f = open('../streetname.txt','r')
food = f.readlines()
f.close()
for i in xrange(len(food)):
    food[i] = food[i].strip()

YOUR_API_KEY = "ce17e2a6-eaa3-47a7-bd16-8a84a7535cf7"
number_of_record = 1000

client = Client(YOUR_API_KEY)
d = {}

for n in xrange(100,1001,100):
#for n in xrange(10,101,10):
    print "***************** " + str(n) + " col writing start ********************"
    starttime=time.time()
    for i in xrange(0,number_of_record):
        for k in xrange (1,n):
            d.update({food[i+k]:food[i+10000+k]})
        #json_data = json.dumps(d)
#        print d
        #print json_data
        response = client.put('acidtest', food[i], d)
    #    response = client.get('acidtest', food[i])
    #    print response.json
    #    print "---------------"
        #response.raise_for_status()

    print str(time.time()-starttime) + "sec"

    print "***************** " + str(n) + " col reading start ********************"
    starttime=time.time()
    for i in xrange(0,number_of_record):
        response = client.get('acidtest', food[i])

    print str(time.time()-starttime) + "sec"

