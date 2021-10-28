from os import X_OK, name
import random
import string

WORD_LIST_FILENAME = r"C:\Users\Leon\Desktop\MIT_6.00.1x\unit4\problem-set-4\words.txt"
word_list = load_words()

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORD_LIST_FILENAME, "r")
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


""" 
Scenarios
1. len(word) = n
    >> using scrabble dictionary, obtain value for each key (char) in word
    >> sum(letter_score) * len(word) + 50
2. len(word) < n
    >> using scrabble dictionary, obtain value for each key (char) in word
    >> sum(letter_score) * len(word)
  """


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # iterates through each letter in word.
    # for each letter, check at the SCRABBLE dictionary to obtiain attached score.
    # sum each score for total.
    # multiple sum by n (length of the word).
    letter_score = [SCRABBLE_LETTER_VALUES.get(key) for key in list(word)]
    if len(word) < n:  # didn't use all letters in hand
        word_score = sum(letter_score) * len(word)
    else:  # used all letters in hand
        word_score = sum(letter_score) * len(word) + 50

    return word_score


""" 
>> iterate through each letter in word. 
>> for each letter, check for that letter in hand and minus 1. 
>> 
"""


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    temp_hand = hand.copy()
    for letter in word:
        temp_hand[letter] = temp_hand.get(letter) - 1
    return temp_hand


hand = {"l": 1, "e": 1, "o": 1, "n": 1}
word = "len"

print(update_hand(hand, word))


# def deal_hand(n):


#     """
#     Returns a random hand containing n lowercase letters.
#     At least n/3 the letters in the hand should be VOWELS.

#     Hands are represented as dictionaries. The keys are
#     letters and the values are the number of times the
#     particular letter is repeated in that hand.

#     n: int >= 0
#     returns: dictionary (string -> int)
#     """
#     hand = {}
#     num_vowels = n // 3

#     for i in range(num_vowels):
#         # x = VOWELS[random.randrange(0, len(VOWELS))]
#         x = random.choice(VOWELS)
#         hand[x] = hand.get(x, 0) + 1

#     for i in range(num_vowels, n):
#         # x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
#         x = random.choice(CONSONANTS + VOWELS)
#         hand[x] = hand.get(x, 0) + 1

#     return hand


""" 
verify validity of the word input by the user.
rules:
>> word is in the word list. 
>> composed entirely of letters from the current hand. 

steps:
>> check if word is in word_list.
>> check the word can be constructed using characters in the hand. 
"""


# def is_valid_word(word, hand, word_list):
#     """
#     Returns True if word is in the word_list and is entirely
#     composed of letters in the hand. Otherwise, returns False.

#     Does not mutate hand or word_list.

#     word: string
#     hand: dictionary (string -> int)
#     word_list: list of lowercase strings
#     """
#     temp_hand = hand.copy()

#     for letter in word:
#         if letter in temp_hand:
#             temp_hand[letter] = temp_hand.get(letter) - 1
#         else:
#             return False

#     if all(value >= 0 for value in temp_hand.values()) and (word in word_list):
#         return True
#     else:
#         return False


# word_list = load_words()
# print(
#     is_valid_word(
#         "honey", {"n": 1, "h": 1, "o": 1, "y": 1, "d": 1, "w": 1, "e": 0}, word_list
#     )
# )


# def calculate_hand_len(hand):
#     """
#     Returns the length (number of letters) in the current hand.

#     hand: dictionary (string-> int)
#     returns: integer
#     """
#     return sum(hand.values())

#     #  alternative method
#     #  return sum([hand[key] for key in hand])

#     # alternative method
#     # hand_len = 0
#     # for key in my_dict:
#     #     hand_len += my_dict[key]
#     # print(hand_len)


# temp_hand = {"l": 1, "e": 1, "o": 1, "n": 2}
# print(calculate_hand_len(temp_hand))




def play_hand(hand, word_list, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    temp_hand = hand.copy()
    total_score = 0
    print(f"Current Hand: {temp_hand}")
    word = input('Enter word, or a "." to indicate you are finished: ')
    while sum(temp_hand) > 0:
        if not word == ".":  # word is entered.
            total_score += get_word_score(word, n)
            update_hand
        else:  # '.' entered >> end game.
            break

    return total_score

    print(word)
    return word


print(play_hand({"l": 1, "e": 1}, word_list, 2))
