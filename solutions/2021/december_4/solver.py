from copy import deepcopy
from itertools import chain
from typing import List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str):
    def build_single_card(bingo_card):
        rtrn_card = []
        for row in bingo_card:
            rtrn_row = row.replace("  ", " ").strip().split(" ")
            rtrn_card.append(rtrn_row)
        return rtrn_card

    bingo_dict = {}
    split_input = raw_puzzle_in.split("\n\n")
    # Get drawings
    bingo_dict["drawings"] = split_input[0].split(",")
    # Build cards
    bingo_card_base = split_input[1:]
    bingo_cards = []
    for card in bingo_card_base:
        cur_card = card.splitlines()
        bingo_cards.append(build_single_card(cur_card))
    bingo_dict["cards"] = bingo_cards
    return bingo_dict


def get_check_string(card_size: int = 5):
    check_strng = ""
    for i in range(card_size):
        check_strng += "!"
    return check_strng


def check_card(bngo_crd: List[List], card_size: int = 5):
    def check_rows(bngo_crd: List[List], card_size: int):
        for i in range(card_size):
            check_list = []
            for j in range(card_size):
                check_list.append(bngo_crd[i][j][0])
            if "".join(check_list) == get_check_string(card_size):
                return (True, (i, j))
        return (False, (-1, -1))

    def check_cols(bngo_crd: List[List], card_size: int):
        for j in range(card_size):
            check_list = []
            for i in range(card_size):
                check_list.append(bngo_crd[i][j][0])
            if "".join(check_list) == get_check_string(card_size):
                return (True, (j, i))
        return (False, (-1, -1))

    def check_diagonals(bngo_crd: List[List], card_size: int):
        diagonal_lst = []
        for i in range(card_size):
            diagonal_lst.append(bngo_crd[i][i][0])
        if "".join(diagonal_lst) == get_check_string(card_size):
            return (True, (i, i))
        return (False, (-1, -1))

    # Check rows
    row_bingo = check_rows(bngo_crd=bngo_crd, card_size=card_size)
    # Check columns
    # transp_crd = list(map(list, zip(*bngo_crd)))
    col_bingo = check_cols(bngo_crd=bngo_crd, card_size=card_size)
    # Check diagonals
    diag_bingo = check_diagonals(bngo_crd=bngo_crd, card_size=card_size)

    if row_bingo[0]:
        return row_bingo
    elif col_bingo[0]:
        return col_bingo
    elif diag_bingo[0]:
        return diag_bingo
    return (False, (-1, -1))


def cross_card(bngo_crd: List[List], card_size: int, cur_draw: str):
    lcl_bngo_crd = bngo_crd
    for i in range(card_size):
        for j in range(card_size):
            if lcl_bngo_crd[i][j] == cur_draw:
                lcl_bngo_crd[i][j] = f"!{lcl_bngo_crd[i][j]}"
    return lcl_bngo_crd


def solve_puzzle_1(puzzle_in) -> None:
    # Puzzle logic:
    #
    # Answer:
    #
    drawings = puzzle_in["drawings"]
    cards = puzzle_in["cards"]
    card_size = len(cards[0][0])

    for drawing in drawings:
        for idx, card in enumerate(cards):
            card = cross_card(
                bngo_crd=card, card_size=card_size, cur_draw=drawing
            )
            crd_check = check_card(bngo_crd=card, card_size=card_size)
            if crd_check[0]:
                card_nr = idx
                winning_drawing = int(drawing)
                flattened_card = chain.from_iterable(card)
                rem_row = [
                    int(entry) for entry in flattened_card if entry[0] != "!"
                ]
                break
        else:
            continue
        break

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Playing with {len(cards)} cards, with size {card_size}")
    print(f"Winning drawing: {winning_drawing} on card: {card_nr+1}")
    print(f"Puzzle awnser: {winning_drawing*sum(rem_row)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in) -> None:
    # Puzzle logic:
    #
    # Answer:
    #
    def run_drawing(drawings, cards):
        for drawing in drawings:
            # print(f"Drawing number: {drawing}!")
            for idx, card in enumerate(cards):
                card = cross_card(
                    bngo_crd=card, card_size=card_size, cur_draw=drawing
                )
                crd_check = check_card(bngo_crd=card, card_size=card_size)
                if crd_check[0]:
                    # First see if there needs to be something removed
                    if len(cards) > 1:
                        return (True, card, -1)
                    # Else calculate the remainder
                    else:
                        return (False, card, int(drawing))
            else:
                continue
            break

    drawings = puzzle_in["drawings"]
    cards = puzzle_in["cards"]
    no_cards = len(puzzle_in["cards"])
    card_size = len(cards[0][0])

    sub_cards = deepcopy(cards)

    play_bingo = True
    while play_bingo:
        result = run_drawing(drawings=drawings, cards=sub_cards)
        play_bingo = result[0]
        if play_bingo:
            sub_cards.remove(result[1])
    winning_drawing = result[2]
    last_winning_card = result[1]
    flattened_card = chain.from_iterable(last_winning_card)
    rem_row = [int(entry) for entry in flattened_card if entry[0] != "!"]

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Playing with {len(cards)} cards, with size {card_size}")
    print(f"Winning drawing: {winning_drawing}!")
    print(f"Puzzle awnser: {winning_drawing*sum(rem_row)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    bingo_inpt = transform_input(aoc_input)
    solve_puzzle_1(deepcopy(bingo_inpt))
    solve_puzzle_2(deepcopy(bingo_inpt))
