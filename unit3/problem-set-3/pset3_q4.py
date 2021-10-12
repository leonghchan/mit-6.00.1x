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


# def hangman(secret_word):
#     loadWords()
#     welcome = textwrap.dedent(
#         f"""\
#     Welcome to the game of Hangman!
#     I am thinking of a word that is {len(secret_word)} letters long."""
#     )
#     print(welcome)

#     guesses_remaining, letters_guessed = 8, []
#     while guesses_remaining > 0:
#         print("-------------------------")
#         if isWordGuessed(secret_word, letters_guessed):  # user wins the game
#             print("Congrats, you won!")
#             return None
#         else:  # game not yet won by user
#             print(f"You have {guesses_remaining} guesses left")
#             print(f"Available Letters: {get_available_letters(letters_guessed)}")
#             guess_str = validity_checker()  # input validation function
#             if (
#                 guess_str in letters_guessed
#             ):  # input value already provided from previous guesses
#                 print(
#                     f"Oops! You've already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}"
#                 )
#             else:  # new input value provided by user
#                 letters_guessed += guess_str
#                 if guess_str in secret_word:  # correct guess
#                     print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
#                 else:  # incorrect guess
#                     guesses_remaining -= 1
#                     print(
#                         f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}"
#                     )
#     print("-------------------")
#     print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
#     return None


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

