#!/usr/bin/python

num = int(raw_input("Give me a number:  "))
num2 = int(raw_input("Give me another number:  "))

if num % 2 == 0:
    if num % 4 == 0:
        print "{} is divisible by four!".format(num)
    else:
        print "{} is even".format(num)
else:
    print "{} is odd".format(num)

if num % num2 == 0:
    print "{} is divisible by {}.".format(num, num2)
else:
    print "{} is not divisible by {}.".format(num, num2)
