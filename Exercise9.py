#!/usr/bin/python

import random

theNumber = random.randint(1, 9)
guesses = 0

while True:
    guess = raw_input("Pick a number between 1 and 9.  Or type exit if you give up. ")
    if guess.lower() == 'exit':
        print "Giving up already? You only guessed {} times.".format(guesses)
        exit()
    else:
        if guess.isdigit():
            guesses += 1
            guess = int(guess)
            if theNumber > guess:
                print "You need to guess a little higher."
            elif theNumber < guess:
                print "You've overestimated the number."
            else:
                print "Boom! On the nose!  It only took you {} guesses!".format(guesses)
                exit()
        else:
            print "You need to guess a number!"

