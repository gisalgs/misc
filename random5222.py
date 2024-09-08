'''
A simple random number generator and some derived functions.

Change history
  Spetember 8, 2024
    First version and release

Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
'''

import time

# Quick and dirty random number generator
# Numerical Recipes in C++, p. 289, eq. 7.1.6

_m = 2**32
_a = 1664525
_c = 1013904223
_X_5222 = int(time.time() * 1000000)

def random():
    global _X_5222
    _X_5222 = (_a*_X_5222 + _c) % _m
    return _X_5222/_m

def randint(a, b):
    '''
    Returns a random integer between a and b, both inclusive.
    '''
    if type(a) != int or type(b) != int:
        raise Exception('Input must be all integers')
    if a > b:
        a, b = b, a
    rand = random()
    diff = b-a+1
    rand = a + rand*diff
    return int(rand)

def uniform(a, b):
    '''
    Returns a random floating point value between a and b.
    '''
    if type(a) != int and type(a) != float or type(b) != int and type(b) != float:
        raise Exception('Input must be either integer or float')
    if a > b:
        a, b = b, a
    global _X_5222
    _X_5222 = (_a*_X_5222 + _c)%_m
    rand = _X_5222/(_m-1)
    diff = b-a
    rand = a + diff*rand 
    return rand