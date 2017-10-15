#!/usr/bin/python


def reverse_str(s):
    return ' '.join(s.split()[::-1])

def reverse_str1(s):
    myStr = s.split()
    retStr = ""
    for w in myStr[::-1]:
        retStr += w + ' '
    return retStr.strip()

def reverse_str2(s):
    myStr = s.split()
    retStr = ""
    for w in range(len(myStr) - 1, -1, -1):
        print myStr[w]

def reverse_str3(s):
    split_str = s.split()
    rev_str = split_str[::-1]
    joined_str = ' '.join(rev_str)
    print joined_str

initStr = raw_input("Please give a string with a lot of words: ")
print reverse_str(initStr)

