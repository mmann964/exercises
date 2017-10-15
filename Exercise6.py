#!/usr/bin/python

myString = raw_input("Can I have a word? ")

print len(myString)
print myString[::-1]


if myString == myString[::-1]:
    print "{} is a palindrome!".format(myString)
else:
    print "{} is not a palindrome.".format(myString)