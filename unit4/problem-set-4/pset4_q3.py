""" 
Problem set 4 - Question 3 - Valid words

However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game.
A valid word is in the word list; and it is composed entirely of letters from the current hand.
Implement the is_valid_word function.

Testing: Make sure the test_isValidWord tests pass.
In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be?
"""


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    temp_hand = hand.copy()

    for letter in word:
        if letter in temp_hand:
            temp_hand[letter] = temp_hand.get(letter) - 1
        else:
            return False

    if all(value >= 0 for value in temp_hand.values()) and (word in word_list):
        return True
    else:
        return False


# word_list = load_words() # from ps4a.py
# print(
#     is_valid_word(
#         "honey", {"n": 1, "h": 1, "o": 1, "y": 1, "d": 1, "w": 1, "e": 0}, word_list
#     )
# )
