#!/usr/bin/python

def genFibo(x):
    fibList = []
    if x > 0:
        fibList.append(1)
        if x >= 2:
            fibList.append(1)
            if x > 2:
                for i in range(2, x ):
                    fibList.append(fibList[i - 1] + fibList[i - 2])

    return fibList

a = int(raw_input("How many Fibonacci numbers would you like me to generate? "))
print genFibo(a)
