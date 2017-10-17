#!/usr/bin/python

import random

word_list = [ 'mamby', 'picture', 'torchiere', 'slider', 'working', 'practical', 'exercise',
              'history', 'barbell', 'vacation', 'resume', 'counter', 'gingerly', 'seventy-five',
              'languishing', 'noisy', 'release', 'quick', 'caymen', 'cajun', 'spice', 'spinster',
              'giraffe', 'sweetheart', 'listing']

def get_word_from_list():
    return word_list[random.randint(0, len(word_list) - 1)]

def generate_password(strength):
    pword = []
    if strength == 'weak':  # get 2 words from the list
        word1 = get_word_from_list()
        word2 = get_word_from_list()
        while word1 == word2:
            word2 = get_word_from_list()
        return word1 + word2
    else:   # strong password.  At least 10 characters, 1 uppercase, 1 lowercase, 1 number, 1 symbol
        char_type = ["letters1", "letters2", "numbers", "symbols"]
        letters1 = "abcdefghijklmnopqrstuvwxyz"
        letters2 = letters1.upper()
        numbers = "0123456789"
        symbols = "!@#$%^&*()~<>"

        p_length = random.randint(10, 16)
        # first character must be a letter
        x = random.randint(0, 1)
        if x == 0:
            pword.append(letters1[random.randint(0, len(letters1) - 1)])

        else:
            pword.append(letters2[random.randint(0, len(letters2) - 1)])


        for i in range(1, p_length):
            x = random.randint(0, len(char_type) - 1)
            if x == 0:
                pword.append(letters1[random.randint(0, len(letters1) - 1)])
            elif x == 1:
                pword.append(letters2[random.randint(0, len(letters2) - 1)])
            elif x == 2:
                pword.append(numbers[random.randint(0, len(numbers) - 1)])
            elif x == 3:
                pword.append(symbols[random.randint(0, len(symbols) - 1)])


    return ''.join(pword)


ptype = raw_input("Do you want a weak or strong password? ").lower()
if ptype[0] == 's':
    print generate_password('strong')
else:
    print generate_password('weak')

exit()

# rank the words in the word list by length, from shortest to longest
# find the shortest word in the list
shortestlen = word_list[0]
wordlengths = {}
wordlength_counter = {}
for w in word_list:
    wordlengths[w] = len(w)
    if len(w) in wordlength_counter:
        wordlength_counter[len(w)] += 1
    else:
        wordlength_counter[len(w)] = 1
    if len(w) < shortestlen:
        shortestlen = len(w)
print shortestlen
print wordlengths
print wordlength_counter

