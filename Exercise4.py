#!/usr/bin/python

val = raw_input("Number, please! ")
x = val.isdigit()
if val.isdigit():
    num = int(val)
else:
    print "Exiting - you need to enter a number!"
    exit(1)

#num = int(raw_input("Number, please! "))
x = range(2, num)
#divisors = []
print "Square root of {} is {}".format(num, num ** .5)

print "Divisors of {}".format(num)
for y in x:
    if num % y == 0:
        print "  {}".format(y)