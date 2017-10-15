#!/usr/bin/python

def removeDups(dupes):
    '''remove the duplicates from the list with set'''
    return list(set(dupes))

def removeDups2(dupes):
    '''remove the duplicates from the list with a loop'''
    c = []
    for i in dupes:
        if i not in c:
            c.append(i)
    return c

dupeList = [ 0, 1, 2, 3, 4, 5, 7, 7, 13, 2, 3]
noDupes = removeDups(dupeList)
noDupes2 = removeDups2(dupeList)

print dupeList
print set(dupeList)
print noDupes
print noDupes2

# find the common items in each list with set
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set(a) & set(b))
print a
print b
print c

s = "Hello world"
s = s.replace(' ', '+')
print s