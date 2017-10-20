#!/usr/bin/python

def get_list(file_name):
    """Returns list of numbers from the file"""
    with open(file_name, "r") as fname:
        content = fname.read()

    l1 = []
    l = content.split("\n")
    for n in l:
        l1.append(int(n))

    return l1

if __name__ == "__main__":
    primes = get_list("primenumbers.txt")
    happy = get_list("happynumbers.txt")
    happyprimes = []

    for n in primes:
        if n in happy:
            happyprimes.append(n)

    print happyprimes
