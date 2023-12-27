from copy import deepcopy
from pathlib import Path

def read_input(is_test: bool = False):
    if is_test:
        input_file = Path("inputs/test.txt")
    else:
        input_file = Path("inputs/actual.txt")

    with open(input_file) as file:
        content = file.read().splitlines()
    
    return content

def transform_input(is_test: bool = False):
    content = read_input(is_test=is_test)

    new_content = dict()

    for row in content:
        split_nr_content = row.split(': ')
        card_number = int(split_nr_content[0].replace('Card ', ''))
        card_content = split_nr_content[1]

        split_win_draw = card_content.split(' | ')
        winning_nrs = set( int(instance) for instance in split_win_draw[0].split())
        drawed_nrs = set( int(instance) for instance in split_win_draw[1].split())

        new_content[card_number] = {
            "winning_nrs": winning_nrs,
            "drawed_nrs": drawed_nrs
        }

    return new_content

def solve_puzzle_1(puzzle_in: dict) -> None:
    puzzle = deepcopy(puzzle_in)

    solution_number = 0

    for v in puzzle.values():
        matches = v["winning_nrs"].intersection(v["drawed_nrs"])
        points = 0
        for i in range(len(matches)):
            if i == 0:
                points += 1
            else:
                points = points * 2
        solution_number += points

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{solution_number}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: dict) -> None:
    puzzle = deepcopy(puzzle_in)
    working_puzzle = list([ [k, v] for k, v in puzzle.items() ])

    card_counting = dict()

    while len(working_puzzle) > 0:
        current_card = working_puzzle.pop()
        card_number = current_card[0]
        wins_and_draws = current_card[1]
        no_wins = len(wins_and_draws["winning_nrs"].intersection(wins_and_draws["drawed_nrs"]))
        extra_cards = [ i + 1 + card_number for i in range(no_wins) ]

        for extra_card in extra_cards:
            working_puzzle.append([extra_card, puzzle[extra_card]])

        if card_number in card_counting:
            card_counting[card_number] += 1
        else:
            card_counting[card_number] = 1
    
    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{sum(card_counting.values())}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input(is_test=False)
    solve_puzzle_2(transfrmd_inp_p2)
