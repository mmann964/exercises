#!/usr/bin/python

import random

def generate_number():
    #num_str = ""
    c = range(0, 10)
    n = random.sample(c, 4)  # a list of 4 unique numbers between 0 and 9
    return n

def get_user_number():
    # get a four digit number from the user.
    # check that it's 4 digits -- length + 0-9
    # give them a chance to exit
    # return number as a string?  list of numbers?
    print "Please guess a 4 digit number.  Type bail if you've had enough."
    while True:
        res = raw_input(">>>>> ").lower().strip()
        if res == "bail":
            print "Thanks for playing! "
            exit()
        elif res.isdigit():
            if len(res) == 4:
                num_list = []
                for i in res:
                    num_list.append(int(i))
                return num_list
            else:
                print "Enter 4 digits."
        else:
            print "That's not a number!"

def eval_nums(tnum, unum):
    # if a digit in unum is in the same place as in tnum, they get a cow
    # if a digit in unum is in tnum, they get a bull
    # return a list: [ cows, bulls ]

    cows = 0
    bulls = 0

    for i in range(0, len(unum)):
        if unum[i] == tnum[i]:
            cows += 1
        elif unum[i] in tnum:
            bulls += 1

    return [ cows, bulls ]


def print_results(ans, guess_count):
    # ans is a list:  [ cows, bulls ]
    # print how many cows and bulls they have
    # if cows = 4, you're done!  print the number of guesses and exit

    print "{} cows, {} bulls.".format(ans[0], ans[1])
    print ""
    if ans[0] == 4:
        print "Congratulations!  It took you {} guesses." .format(guess_count)
        exit()


if __name__ == "__main__":
    the_num =  generate_number()
    print the_num

    guesses = 0
    while True:
        user_num = get_user_number()
        guesses += 1
        answer = eval_nums(the_num, user_num)
        print_results(answer, guesses)