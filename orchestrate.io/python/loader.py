#!/usr/bin/python
# -*- coding: utf-8 -*-

from porc import Client
import random
import math
import datetime
import hashlib
import sys

def zipf(max):
    return math.e ** (random.random() * math.log(max + 1.0)) - 1.0

def generator(num,offset):
    r = int(zipf(num)) + offset
    txt = hashlib.sha512(str(r)).hexdigest()
    txt = txt+txt+txt+txt+txt+txt+txt+txt
    txt = txt[0:txt.find('a')+txt.find('b')+10]
    return txt

def strrnd(st, num):
    if random.random() > num:
        s = st[0]
    else:
        s = st[1]
    return s

def intrnd(min, max):
    return str(int(round(random.random()*(max-min)))+min)

def intrnds(min, max, format):
    return ("{0:" + format + "}").format(int(round(random.random()*(max-min)))+min)

def floatrnd(min, max):
    return str(random.random()*(max-min)+min)

def nullgen(st, num):
    if random.random() < num:
        return ''
    else:
        return st

def daternd(min, max):
    mindate = datetime.datetime.strptime(min,'%Y/%m/%d')
    maxdate = datetime.datetime.strptime(max,'%Y/%m/%d')
    return datetime.datetime.strftime(mindate + datetime.timedelta(days=random.random()*(maxdate-mindate).days), '%Y/%m/%d')

def log_gen():
    time_x = datetime.datetime.strftime(datetime.datetime.strptime('2013-11-30 00:00:00','%Y-%m-%d %H:%M:%S') + datetime.timedelta(seconds=random.random()*3600*24),'%Y-%m-%d %H:%M:%S')
    key_id = str(int(zipf(60000000)+10000000000))
    col_001 = str(int(random.random()*20))
    col_002 = str(440)
    col_003 = nullgen('http:',0.3)
    col_004 = nullgen(generator(15000000, 15000000),0.3)
    col_005 = nullgen(generator(10000000000, 10000000000),0.3)
#    col_006 = hashlib.md5(str(int(zipf(15000000)))).hexdigest()
    col_006 = str(int(random.random()*253+1)) + '.' + str(int(random.random()*253+1)) + '.' + str(int(random.random()*253+1)) + '.' + str(int(random.random()*253+1))
    col_007_tmp = int(random.random()*10000)
    col_007 = str(col_007_tmp)
    col_008 = str(int(col_007_tmp*random.random()*10))
    col_009 = str(16)
    col_010 = hashlib.md5(str(int(zipf(100))+98765)).hexdigest()
    col_011 = generator(15000000, 30000000)
#        col_012 = '/'
    col_012 = nullgen(generator(10000000000, 10000000000),0.01)
#        col_013 = ''
    col_013 = nullgen("".join([random.choice(source_str) for x in xrange(4)]),0.3)
    col_014 = str(2)
#    col_015 = hashlib.md5(str(int(zipf(15000000)))).hexdigest()
    col_015 = str(int(random.random()*253+1)) + '.' + str(int(random.random()*253+1)) + '.' + str(int(random.random()*253+1)) + '.' + str(int(random.random()*253+1))
    col_016 = str(int(random.random()*65535))
    col_017 = str(int(random.random()*65535))
    col_018 = '0'
    if random.random()>0.5:
        col_019 = generator(10000000000, 1)+generator(10000000000, 1)
    else:
        col_019 = ''

    record = [time_x,key_id,col_001,col_002,col_003,col_004,col_005,col_006,col_007,col_008,col_009,col_010,col_011,col_012,col_013,col_014,col_015,col_016,col_017,col_018,col_019]
    return record


if __name__ == "__main__":
    YOUR_API_KEY = "ce17e2a6-eaa3-47a7-bd16-8a84a7535cf7"
    client = Client(YOUR_API_KEY)
