""" 
Problem set 4 - Question 6 - Playing a Game

A game consists of playing multiple hands.
We need to implement one final function to complete our word-game program.
Write the code that implements the playGame function. 
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
    deal_hand,
    display_hand,
    update_hand,
    is_valid_word,
    calculate_hand_len,
    play_hand,
)


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    while True:
        user_option = input(
            "Enter n to deal a new hand, r to replay the last hand, or e to end game:"
        )
        if user_option == "n":  # new game
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif user_option == "r":  # replay last hand
            try:
                play_hand(hand, word_list, HAND_SIZE)
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        elif user_option == "e":  # end game
            break
        else:  # invalid
            print("Invalid command ")
        print()


# word_list = load_words()
# HAND_SIZE = 15
# print(play_game(word_list))

