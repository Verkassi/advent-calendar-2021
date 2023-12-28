from copy import deepcopy
from pathlib import Path
from time import time
from collections import Counter

# Determine the strength of single cards
# CARD_ORDER = tuple(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
# If the Hand Strength in both hands are equal, the highest first card in the hand wins
# If those are equal, the second one in the hand wins
# etc. etc.

def read_input(is_test: bool = False, split_lines: bool = True):
    if is_test:
        input_file = Path("inputs/test.txt")
    else:
        input_file = Path("inputs/actual.txt")

    with open(input_file) as file:
        if split_lines:
            content = file.read().splitlines()
        else:
            content = file.read()
    return content

def convert_input(is_test: bool = False, split_lines: bool = True):
    input_rows = read_input(is_test=is_test, split_lines=split_lines)

    input_data = [ row.split() for row in input_rows ]

    hand_to_bid = dict()
    for row in input_data:
        hand_to_bid[row[0]] = int(row[1])
    hands = [ row[0] for row in input_data ]

    return (input_data, hands, hand_to_bid)


def sort_hand_types(hands: list):

    def _calculate_hand_type(hand: str):
        cards = [ card for card in hand ]
        card_occurances = Counter(cards).values()

        if {1} == set(card_occurances):
            return "High card"
        elif 5 in card_occurances:
            return "Five of a kind"
        elif 4 in card_occurances:
            return "Four of a kind"
        elif (3 in card_occurances) and (2 in card_occurances):
            return "Full house"
        elif 3 in card_occurances:
            return "Three of a kind"
        elif 2 in Counter(card_occurances).values():
            return "Two pair"
        elif 2 in card_occurances:
            return "One pair"
        else:
            raise ValueError("Can't determine what type of hand this is!")

    hands_by_type = { hand_type: [] for hand_type in tuple(["Five of a kind", "Four of a kind", "Full house", "Three of a kind", "Two pair", "One pair", "High card"]) }

    for hand in hands:
        hand_instance = _calculate_hand_type(hand)
        hands_by_type[hand_instance].append(hand)

    return hands_by_type

def sort_hands_in_type(hands: list, card_to_value_conversion = dict[str: int]):
    numbers_to_cards = {v: k for k, v in card_to_value_conversion.items()}

    cards_all_numbers = [ [ card_to_value_conversion[card] for card in hand ] for hand in hands ]
    cards_all_numbers = sorted(cards_all_numbers, reverse=True)
    sorted_hands = [ [ numbers_to_cards[card] for card in hand ] for hand in cards_all_numbers ]

    return sorted_hands

def solve_puzzle_1(puzzle_in: list) -> None:
    # get the start time
    st = time()

    # Solve Puzzle
    hands_with_bids, hands, hand_to_bid = deepcopy(puzzle_in)

    # Simple card conversion
    cards_to_number = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9 ,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    # Sort the hands based on their strength
    typed_hands = sort_hand_types(hands=hands)

    sorted_hands = list()
    for hand_type, hands in typed_hands.items():
        sorted_typed_hands = sort_hands_in_type(hands=hands, card_to_value_conversion=cards_to_number)
        sorted_hands.extend(sorted_typed_hands)
    
    complete_hands = [ "".join(hand) for hand in sorted_hands ]

    # Multipy the bid of each hand by their rank in strenght
    bids = [ hand_to_bid[hand] * (len(complete_hands) - (i)) for i, hand in enumerate(complete_hands) ]

    # get the end time
    et = time()

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    # Total winnings is the sum of the multiplied bids
    print(sum(bids))
    print("------------------- RUN DURATION --------------------")
    print('Execution time:', round(st - et, 2), 'seconds')
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # get the start time
    st = time()

    # Solve Puzzle
    hands_with_bids, hands, hand_to_bid = deepcopy(puzzle_in)

    # Simple card conversion
    cards_to_number = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
        "T": 10,
        "9": 9 ,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }
    numbers_to_cards = {v: k for k, v in cards_to_number.items()}

    # Convert all cards to numbers
    cards_all_numbers = [ [ cards_to_number[card] for card in hand ] for hand in hands ]
    # print(cards_all_numbers)

    # Convert all Jokers to strongest match in hand
    hands_joker_conversion = list()
    for hand in cards_all_numbers:
        cards_joker_conversion = [ max(hand) if card == 1 else card for card in hand ]
        hands_joker_conversion.append(cards_joker_conversion)
    # print(hands_joker_conversion)

    # TODO: I want to get to the following construction: { "joker_hand_1": "original_hand_1", "joker_hand_2": "original_hand_2" }
    backwards_conversion = { joker_hand: original_hand  } ## TODO: THIS SHOULD BE FULL HANDS FIRST, ELSE THIS WILL NOT WORK
    # Matches between original hand and joker converted hands
    # conver_back_to_original_hand = { hands_joker_conversion[i]: cards_all_numbers[i] for i, hand in enumerate(cards_all_numbers)  }

    # hand_with_conversions = list(zip(cards_all_numbers, hands_joker_conversion))

    print(conver_back_to_original_hand)
    # print(sorted(hand_with_conversions))

    # Sort the hands based on their strength
    typed_hands = sort_hand_types(hands=hands)



    # get the end time
    et = time()

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(typed_hands)
    print("------------------- RUN DURATION --------------------")
    print('Execution time:', round(st - et, 2), 'seconds')
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = convert_input(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = convert_input(is_test=True)
    solve_puzzle_2(transfrmd_inp_p2)
