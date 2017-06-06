# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 17:56:48 2017
@author: Gin
"""
''' Assignment 14.1
This application will read the mailbox data (mbox.txt) count up the number 
email messages per organization (i.e. domain name of the email address) using 
a database with the following schema to maintain the counts.'''
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
