""" 
Problem set 3 - Problem 4 - The Game

Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess.
This starts up an interactive game of Hangman between the user and the computer.
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick arandom one.
Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor.
When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:
guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:
secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed.
Every time a player guesses a letter, the guessed letter must be removed from availableLetters
(and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters,
you do not need to paste your definitions in the box.
We have supplied our implementations of these functions for your use in this part of the problem.
If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.

"""


from typing import Counter
from pset3_hangman import (
    get_available_letters,
    get_guessed_word,
    is_word_guessed,
    load_words,
)
import textwrap
import re
import sys


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
        print(f"You have {guesses_remaining} guesses left")
        print(f"Available Letters: {get_available_letters(letters_guessed)}")
        guess_str = validity_checker()  # input validation function, returns valid guess
        if guess_str not in letters_guessed:  # new input value provided by user
            letters_guessed += guess_str
            if guess_str in secret_word:  # correct guess
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            else:  # incorrect guess
                guesses_remaining -= 1
                print(
                    f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}"
                )
        else:  # input value already provided from previous guesses
            print(
                f"Oops! You've already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}"
            )
        if is_word_guessed(secret_word, letters_guessed):  # user wins the game
            print("Congrats, you won!")
            return None
    print("-------------------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
    return None


# print(hangman("a"))

