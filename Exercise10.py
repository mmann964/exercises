#!/usr/bin/python

import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(20), random.randint(1, 20))
b = random.sample(range(20), random.randint(1, 20))

#evens = [ x for x in a if x % 2 == 0]

c = [ x for x in a if x in b ]
d = []
for i in c:
    if i not in d:
        d.append(i)

print a
print b
print c
print d