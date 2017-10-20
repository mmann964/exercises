#!/usr/bin/python

import random

def generateOrderedList():
    """returns a list with a random number (between 1 and 20)
     of random integers between 0 and 199"""

    num_items = random.randint(1, 20)
    l = sorted(random.sample(range(200), num_items))
    return l

def is_it_here(n, l):
    """Does a binary search to see if number n is in list l - returns True or False"""
    # print n
    # print l

    if n == l[len(l)/2 - 1]:
        return True
    elif n < l[0]:
        return False
    elif n > l[len(l) - 1]:
        return False
    elif n < l[len(l)/2 - 1]:
        return is_it_here(n, l[0:len(l)/2])
    else:
        return is_it_here(n, l[len(l)/2:])



if __name__ == "__main__":
    my_list = generateOrderedList()
    my_num = random.randint(0, 200)
    print "Is {} in {} ?" .format(my_num, my_list)
    print is_it_here(my_num, my_list)
