# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 17:41:57 2017

@author: Gin
"""

''' Assignment 6.5 
This code using find() and string slicing (see section 6.10) 
to extract the number at the end of the line below. Convert the extracted value 
to a floating point number and print it out.'''

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