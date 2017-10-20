#!/usr/bin/python

import random

## Five numbers:  1 - 47 + Mega: 1 - 27
# Determine how many of the 5 numbers match
# Determine if the Mega number matches

## More ideas:  keep track of how much you spent vs won
## See how long it takes to win more than you spent

def generate_5_numbers():
    """Return a list of 5 random numbers between 1 and 47"""

    l = sorted(random.sample(range(1, 48), 5))
    return l

def generate_mega():
    """Generate a random number between 1 and 27"""
    return random.randint(1, 27)

def check_ticket(l, n):
    """Print how many numbers match and if the mega matches"""

    print l, n

    i = 0
    for num in l:
        if num in winners:
            i += 1

    mega_match_str = ""
    mega_match = False
    if n == mega:
        mega_match = True
        mega_match_str = "+ Mega!"

    matches_str = "matches"
    if i == 1:
        matches_str = "match"

    winnings = find_winnings(i, mega_match)

    print "{} {} {}".format(i, matches_str, mega_match_str)
    print "You won: $ {}".format(winnings)

    return winnings

def find_winnings(matches, megamatch):
    """determines the winnings"""

    if matches == 5 and megamatch:
        winnings = 23000000
    elif matches == 5:
        winnings = 35461
    elif matches == 4 and megamatch:
        winnings = 1611
    elif matches == 4:
        winnings = 94
    elif matches == 3 and megamatch:
        winnings = 45
    elif matches == 3:
        winnings = 9
    elif matches == 2 and megamatch:
        winnings = 8
    elif matches > 0:
        winnings = 1
    elif megamatch:
        winnings = 1
    else:
        winnings = 0

    return winnings

if __name__ == "__main__":

    bank = 1000
    year = 0

    while bank > 0:
        year += 1
        biggest_ticket = 0
        winning_tickets = {}

        print "You're starting with ${}".format(bank)
        for week in range(52):
            if bank <= 0:
                break
            winners = generate_5_numbers()
            mega = generate_mega()

            print "***** Winning Numbers for Year {} - Week {} *****".format(year, week + 1)
            print winners, mega

            print "---- Your Numbers ----"
            for qp in range(5):
                if bank <= 0:
                    break
                bank -= 1
                my_nums = generate_5_numbers()
                my_mega = generate_mega()

                winnings = check_ticket(my_nums, my_mega)
                bank += winnings
                print "You have ${} ".format(bank)
                if winnings > biggest_ticket:
                    biggest_ticket = winnings
                if str(winnings) in winning_tickets:
                    winning_tickets[str(winnings)] += 1
                else:
                    winning_tickets[str(winnings)] = 1

        print "-----------------------------------"
        print "You ended up with ${}".format(bank)
        print "Your biggest ticket was worth ${}".format(biggest_ticket)
        print winning_tickets

print "It took {} years to lose your $1000".format(year)

