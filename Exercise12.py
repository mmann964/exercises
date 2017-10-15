#!/usr/bin/python

def firstAndLast(b):
    l = []
    l.append(b[0])
    l.append(b[-1])
    return l

def firstAndLast2(b):
    return [ b[0], b[-1]]

a = [ 5, 10, 15, 20, 32, 19 ]
print firstAndLast2(a)

