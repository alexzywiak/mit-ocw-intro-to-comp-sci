#!/usr/bin/env python -tt
# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
import re

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def is_word_frag(sub_str):

    for word in wordlist:
        if word[:len(sub_str)] == sub_str:
            return True
    return False

def is_word(word):
    return word in wordlist and len(word) > 3

def is_valid_input(ch):
    if len(ch) > 1 or not re.match('[A-Za-z]', ch):
        return False
    else:
        return True


def play_game():
    p1 = raw_input('Player One name: ')
    p2 = raw_input('Player Two name: ')
    players = (p1, p2)
    
    turn = 0
    word = ''

    while is_word_frag(word) and not is_word(word):

        valid_input = False

        while not valid_input:
            print 'Word So Far: ' + word
            ch = raw_input(players[turn] + ' add a letter: ')

            if is_valid_input(ch):
                word += ch
                turn = 0 if turn == 1 else 1
                valid_input = True
            else:
                print 'Don\'t be playing that game...'

    print 'Final word ' + word
    if not is_word_frag(word):
        print 'No words start with '  + word
    if is_word(word):
        print word + ' is a word!'
    print players[turn] + ' is the winner!'


if __name__ == '__main__':
    play_game()















