"""
Problem set 3 - Question 3 - Printing Out all Available Letters

Next, implement the function get_available_letters that takes in one parameter - a list of letters, letters_guessed.
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in letters_guessed.

Example Usage:
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(get_available_letters(letters_guessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
"""

import string


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    return "".join(
        char for char in string.ascii_lowercase if char not in letters_guessed
    )
    # return "".join(sorted(set(string.ascii_lowercase).difference(letters_guessed)))
    # return "".join(sorted(set(string.ascii_lowercase) - set(letters_guessed)))


# print(get_available_letters(["a", "b", "a"]))

