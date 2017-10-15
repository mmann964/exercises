#!/usr/bin/python

s = "hello world"
d = {}

# count the number of times each character occurs in a string
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

# print the results
# this prints them using the string
for c in s:
    print c, d[c]

print ""

# this prints them by character
for c in d:
    print c, d[c]