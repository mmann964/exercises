#!/usr/bin/python

while True:
    num = raw_input("Give me a number! ")
    if num.isdigit():
        sum = 0
        for n in num:
            sum += int(n)

        if sum % 3 == 0:
            if num == "666":
                print "{} is divisible by 3.  Yay! But it's still the mark of the Beast!".format(num)
            else:
                print "{} is divisible by 3.  Yay!".format(num)
        else:
            print "{} isn't divisible by 3.  Boo. :-/".format(num)

    else:
        exit()