# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 19:33:26 2017

@author: Gin
"""

''' Assignment 13.1
This program prompt for a URL, read the XML data from that URL using urllib 
and then parse and extract the comment counts from the XML data, 
compute the sum of the numbers in the file.'''
import urllib
import xml.etree.ElementTree as ET

address = "http://python-data.dr-chuck.net/comments_232915.xml"
uh = urllib.urlopen(address)
data = uh.read()
#print data
tree = ET.fromstring(data)
print 'tree', tree
counts = tree.findall('comments/comment')
#print 'counts',counts
sum=0
for count in counts:
    num= count.find('count').text
    sum= sum+ int(num)
print 'sum',sum
