#!/usr/bin/python

def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

a = int(raw_input("Number please! "))
if isPrime(a):
    print "{} is a prime number.".format(a)
else:
    print "{} is not a prime number.".format(a)

