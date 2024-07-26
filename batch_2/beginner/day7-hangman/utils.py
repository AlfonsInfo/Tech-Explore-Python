import  word as w
import random

def random_word():
    """Return a random word from the word list"""
    return random.choice(w.hangman_word_list)


def create_blanks(word):
    blanks = ["_"] * len(word)
    has_blank = False

    for i in range(len(word)):
        if random.randint(1, 3) == 1:
            blanks[i] = "_"
            has_blank = True
        else:
            blanks[i] = word[i]
    
    # Ensure there is at least one blank
    if not has_blank:
        random_index = random.randint(0, len(word) - 1)
        blanks[random_index] = "_"
    
    return blanks

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele + " "
    # return string
    return str1
def message():
    print("Welcome to Hangman Game")
    print("Guess the word by guessing the letters")
    print("You have 6 lives")
    print("Goodluck!")