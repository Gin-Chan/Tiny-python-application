# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 19:31:10 2017

@author: Gin
"""

'''Assignment 13.2
This program prompt for a URL, read the JSON data from that URL using urllib and then parse 
and extract the comment counts from the JSON data, compute the sum of the 
numbers in the file and enter the sum below:'''
import urllib
import json
address = "http://python-data.dr-chuck.net/comments_232919.json"
uh = urllib.urlopen(address)
data = uh.read()
try:info = json.loads(data)
except: info=None
print 'User count:', len(info)
sum=0
for item in info['comments']:
    print 'Name', item['name']
    print 'count', item['count']
    sum = sum + int(item['count'])
print sum