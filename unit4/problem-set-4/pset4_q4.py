""" 
Problem set 4 - Question 4 - Hand length

Implement the helper calculate_hand_len function. 
"""

def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

    #  alternative method
    #  return sum([hand[key] for key in hand])

    # alternative method
    # hand_len = 0
    # for key in my_dict:
    #     hand_len += my_dict[key]
    # print(hand_len)