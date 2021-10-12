# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

from typing import Counter
import textwrap
import re
import sys

# WORDLIST_FILENAME = r"C:\Users\Leon\Desktop\MIT_6.00.1x\words.txt"
# WORDLIST_FILENAME = "C:\\Users\\Leon\\Desktop\\MIT_6.00.1x\\words.txt"
WORDLIST_FILENAME = "C:/Users/Leon/Desktop/MIT_6.00.1x/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    return all({True if char in letters_guessed else False for char in secret_word})
    # (or) return True if sorted(list(set(secret_word))) == sorted(letters_guessed) else False


# print(is_word_guessed("apple", ["a", "p", "l", "e"]))


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    return " ".join([char if char in letters_guessed else "_" for char in secret_word])


# print(get_guessed_word("apple", ["a", "l", "e"]))


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    return "".join(
        [char if char not in letters_guessed else "" for char in string.ascii_lowercase]
    )


# get_available_letters(["a", "p", "l", "e"])


def validity_checker():
    """
    Input validation checker. Ensures the input value by the user 
    is a single character in the alphabet. 
    If the input value is not valid, the user will be requested to 
    provide a valid input.
    """
    while True:
        value = input("Please guess a letter: ").lower()
        try:
            if not re.match("^[a-z]*$", value) or len(value) > 1:
                raise ValueError
        except ValueError:
            print("Please enter one character in the alphabet a-z.")
            print("-------------------------")
            continue
        else:
            break
    return value


def hangman(secret_word):
    """
  secret_word: string, the secret word to guess.

  Starts up an interactive game of Hangman.

  * At the start of the game, let the user know how many 
    letters the secretWord contains.

  * Ask the user to supply one guess (i.e. letter) per round.

  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computers word.

  * After each round, you should also display to the user the 
    partially guessed word so far, as well as letters that the 
    user has not yet guessed.

  Follows the other limitations detailed in the problem write-up.
  """
    load_words()
    welcome = textwrap.dedent(
        f"""\
    Welcome to the game of Hangman!
    I am thinking of a word that is {len(secret_word)} letters long."""
    )
    print(welcome)

    guesses_remaining, letters_guessed = 8, []
    while guesses_remaining > 0:
        print("-------------------------")
        if is_word_guessed(secret_word, letters_guessed):  # user wins the game
            print("Congrats, you won!")
            return None
        else:  # game not yet won by user
            print(f"You have {guesses_remaining} guesses left")
            print(f"Available Letters: {get_available_letters(letters_guessed)}")
            guess_str = validity_checker()  # input validation function
            if (
                guess_str in letters_guessed
            ):  # input value already provided from previous guesses
                print(
                    f"Oops! You've already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}"
                )
            else:  # new input value provided by user
                letters_guessed += guess_str
                if guess_str in secret_word:  # correct guess
                    print(
                        f"Good guess: {get_guessed_word(secret_word, letters_guessed)}"
                    )
                else:  # incorrect guess
                    guesses_remaining -= 1
                    print(
                        f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}"
                    )
    print("-------------------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
    return None


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)

# secret_word = choose_word(wordlist).lower()
# print(hangman("boss"))
