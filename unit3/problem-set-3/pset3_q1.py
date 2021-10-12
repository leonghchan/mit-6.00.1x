"""
Problem set 3 - Question 1

Please read the Hangman Introduction before starting this problem.
We'll start by writing 3 simple functions that will help us easily code the Hangman problem.
First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed.
This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:
>>> secret_word = 'apple'
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(is_word_guessed(secret_word, letters_guessed))
False

For this function, you may assume that all the letters in secret_word and letters_guessed are lowercase.
"""


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    return all({char in letters_guessed for char in secret_word})
    # return set(secret_word).issubset(letters_guessed)


# print(is_word_guessed("apples", ["a", "p", "l", "e", "s"]))
