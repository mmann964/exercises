#!/usr/bin/python

import random

def tryAgain():
    answer = raw_input("Try again? (Y/N) ").lower()
    if answer == "n":
        print "Nice playing with you. Until next time..."
        exit()
    elif answer != "y":
        print "Please enter Y or N."
        tryAgain()

while True:
    guess = raw_input("Rock, Paper, or Scissors? ").lower()

    myList = [ "rock", "paper", "scissors" ]

    if guess not in myList:
        print "You can only pick Rock, Paper, or Scissors."
        continue

    x = random.randint(0, len(myList) - 1)
    computerGuess =  myList[x]
    if guess == "rock":
        if computerGuess == "scissors":
            print "{} beats {}.  You win! ".format(guess, computerGuess)
        elif computerGuess == "paper":
            print "{} beats {}.  Sorry, you lose. ".format(computerGuess, guess)
        else:
            print "We both picked {} -- it's a tie. ".format(guess)
    elif guess == "paper":
        if computerGuess == "rock":
            print "{} beats {}.  You win! ".format(guess, computerGuess)
        elif computerGuess == "scissors":
            print "{} beats {}.  Sorry, you lose. ".format(computerGuess, guess)
        else:
            print "We both picked {} -- it's a tie. ".format(guess)
    elif guess == "scissors":
        if computerGuess == "paper":
            print "{} beats {}.  You win! ".format(guess, computerGuess)
        elif computerGuess == "rock":
            print "{} beats {}.  Sorry, you lose. ".format(computerGuess, guess)
        else:
            print "We both picked {} -- it's a tie. ".format(guess)
    else:
        print "I'm not sure how we got here."

    tryAgain()











