""" 
Problem set 4 - Question 5 - Playing a hand
"""
import random
import string
from ps4a import (
    VOWELS,
    CONSONANTS,
    SCRABBLE_LETTER_VALUES,
    WORD_LIST_FILENAME,
    load_words,
    get_word_score,
    display_hand,
    update_hand,
    is_valid_word,
    calculate_hand_len,
)


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
    while calculate_hand_len(temp_hand) > 0:
        print("Current Hand:", end=" ")
        display_hand(temp_hand)
        word = input(
            'Enter word, or a "." to indicate that you are finished:'
        )  # ask user to input word
        if word != ".":  # input is a word
            if is_valid_word(word, temp_hand, word_list):  # valid word
                total_score += get_word_score(word, len(word))
                print(
                    f'"{word}" earned {get_word_score(word, len(word))} points. Total: {total_score} points'
                )
                temp_hand = update_hand(temp_hand, word)
                print()
            else:  # invalid word
                print("Invalid word, please try again.")
                # print()
        else:  # input is a "."
            print(f"Goodbye! Total score: {total_score} points")
            print()
            return None

    print(f"Run out of letters: Total score: {total_score} points.")


# word_list = load_words()
# print(play_hand({"n": 1, "e": 1, "t": 1, "a": 1, "r": 1, "i": 2}, word_list, 7))
# play_hand({"h": 1, "i": 1, "c": 1, "z": 1, "m": 2, "a": 1}, word_list, 7)
