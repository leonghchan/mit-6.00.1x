#
# Problem7: Play game with computer and user
#

from ps4a import *
from ps4b import *
import time


# def play_game(word_list, hand={}):
#     who = ans = input("Enter n for new hand, r to replay, e to end: ")
#     if ans == "n" or (ans == "r" and hand):
#         hand = hand if ans == "r" else deal_hand(HAND_SIZE)
#         while who not in "uc":
#             who = input("Enter u to play, c for the computer to play: ")
#             play_hand(hand, word_list, HAND_SIZE) if who == "u" else comp_play_hand(
#                 hand, word_list, HAND_SIZE
#             ) if who == "c" else print("Invalid command")
#     print(
#         "Please play a new hand first!\n"
#         if ans == "r" and not hand
#         else "Invalid command.\n"
#         if ans not in "nre"
#         else "",
#         end="",
#     )
#     return None if ans == "e" else play_game(word_list, hand)


def play_game(word_list, hand={}):
    who = ans = input("Enter n for new hand, r to replay, e to end: ")
    if ans == "n" or (ans == "r" and hand):
        hand = hand if ans == "r" else deal_hand(HAND_SIZE)
        while who not in "uc":
            who = input("Enter u to play, c for the computer to play: ")
            play_hand(hand, word_list, HAND_SIZE) if who == "u" else comp_play_hand(
                hand, word_list, HAND_SIZE
            ) if who == "c" else print("Invalid command")
    print(
        "Please play a new hand first!\n"
        if ans == "r" and not hand
        else "Invalid command.\n"
        if ans not in "nre"
        else "",
        end="",
    )
    return None if ans == "e" else play_game(word_list, hand)


# word_list = load_words()
# HAND_SIZE = 10
# print(play_game(word_list))
