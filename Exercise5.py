#!/usr/bin/python

import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def populateList():
    '''Populates listName with a random number (between 1 and 100) of numbers between 1 and 100'''
    listName = []
    numItems = random.randint(1, 100)
    for x in range(0, numItems):
        listName.append(random.randint(1, 100))
    return listName

a = []
b = []
c = []
a = populateList()
b = populateList()
print "a = {}".format(a)
print "b = {}".format(b)

if len(a) < len(b):
    for x in a:
        if x in b:
            if x not in c:
                c.append(x)
else:
    for x in b:
        if x in a:
            if x not in c:
                c.append(x)

print "Entries in both lists: {}".format(c)
