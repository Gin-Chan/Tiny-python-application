# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 19:37:55 2017

@author: Gin
"""
'''This file consists of several program for the practice purpose of learning
Python'''
#14.1
#This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain
#name of the email address) using a database with the following schema to maintain the counts.
import sqlite3
import re
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

#cur.execute('''
#CREATE TABLE Counts (email TEXT, count INTEGER)''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    #y = re.findall('@([^ ]*?)\.',pieces[1])
    y = re.findall('@([^ ]*)',pieces[1])
    org = y[0]
    print org
    #print email
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (org, ))
    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()



#13.3
#prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

   try: js = json.loads(str(data))
   except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue
    print json.dumps(js, indent=4)
    place_id = js["results"][0]["place_id"]
    print place_id


#13.2
#prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
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

#13.1
#prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
import urllib
import xml.etree.ElementTree as ET

address = "http://python-data.dr-chuck.net/comments_232915.xml"
uh = urllib.urlopen(address)
data = uh.read()
print data
tree = ET.fromstring(data)
print 'tree', tree
counts = tree.findall('comments/comment')
print 'counts',counts
sum=0
for count in counts:
    num= count.find('count').text
    sum= sum+ int(num)
print 'sum',sum


#12.3
# Note - this code must run in Python 2.x and you must download http://www.pythonlearn.com/code/BeautifulSoup.py Into the same folder as this program

import urllib
from BeautifulSoup import *
url = raw_input('Enter url- ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Kadin.html"
count =  raw_input('Enter count- ')
position =  raw_input('Enter position- ')
position=int(position)-1
count=int(count)
for i in range(0,count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    url= tags[position].get('href', None)
    print url
    print i
    for tag in tags:
        tag.get('href', None)


#12.2
# Note - this code must run in Python 2.x and you must download http://www.pythonlearn.com/code/BeautifulSoup.py Into the same folder as this program

import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_232918.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
y=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    y= y + int(tag.contents[0])
print y


#12.1
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()


#11,2
import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "extracting data.txt"
handle = open(name)
x=list()
y=list()
total=0
for line in handle:
    x=re.findall('[0-9]+',line)
    y=y+x
for word in y:
    total = total + int(word)
print total

#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
find = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        list = line.split()
        line2 = list[5]
        line2 = line2[:2]
        try:
            find[line2] = find.get(line2,0) + 1
        except:print 'erro'
T = find.items()
T.sort()
for (h,t) in T:
    print h,t

#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
find = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        list = line.split()
        print list[1]
        try:
            find[list[1]] = find.get(list[1],0)+1
        except:print 'erro'
bigcount = None
bigword = None
for key,value in find.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key
print bigword,bigcount


#8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line: You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. Hint: make sure not to include the lines that start with 'From:'.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        list = line.split()
        print list[1]
        count = count+1
print "There were", count, "lines in the file with From as the first word"


#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
fh = open(fname)
list1 = list()
list2 = list()
for line in fh:
    line =line.rstrip()
    print line.rstrip()
    list1 = line.split()
    try:
        for word in list1:
            if word not in list2:
                list2.append(word)
    except:
        print 'error'
    list2.sort()
print list2


# 7.2 Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
c = 0
x=0
y=0
inp = "X-DSPAM-Confidence:"
t=inp.find(':')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    inp = line
    inp = inp[t+1:]
    x = float(inp)
    y=y+x
    c=c+1
print "Average spam confidence:" ,y/c


#7.1 Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp=inp.rstrip()
print inp.upper()


x = 0
if x<2:
    print 'small'
elif x<10:
    print 'medium'
else:
    print 'large'
print 'all done'
quit()


# Assignment 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = 'X-DSPAM-Confidence:    0.8475'
try:
    n = len(text)
    print n
    a = text.find(':')
    print a
    b = text[a+1:]
    print float(b)

except :
    print 'error'