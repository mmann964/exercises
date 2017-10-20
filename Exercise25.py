#!/usr/bin/python

def get_ans(prompt, valid_responses):
    while True:
        ans = raw_input(prompt).lower().strip()
        if len(ans) > 0 and ans[0] in valid_responses:
            return ans[0]

if __name__ == "__main__":
    guesses = 0
    print("Think of a number between 1 and 100...")

    low_guess = 1
    high_guess = 100
    while True:
        guesses += 1
        guess = ((high_guess - low_guess) / 2 ) + low_guess
        ans = get_ans("Is your number {}? ".format(guess), ['y', 'n'])
        if ans == 'y':
            if guesses == 1:
                print "It only took me {} try to guess your number!".format(guesses)
            else:
                print "It only took me {} tries to guess your number!".format(guesses)
            exit()
        elif ans == 'n':
            ans = get_ans("Is your number higher or lower than {}? ".format(guess), ['h', 'l'])
            if ans == 'h':
                # guess the upper part
                low_guess = guess + 1
            elif ans == 'l':
                # guess the lower part
                high_guess = guess - 1



