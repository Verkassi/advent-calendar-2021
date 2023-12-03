from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input

def split_rucksack(whole_sack: str) -> List[str]:
    # Calc slices
    total_length = len(whole_sack)
    first_slice = slice(0,total_length//2)
    second_slice = slice(total_length//2, total_length)

    # Slice strings
    first_pack = whole_sack[first_slice]
    second_pack = whole_sack[second_slice]

    # Return
    return [first_pack, second_pack]

def determine_priority(input_string: str) -> int:
    if input_string == input_string.lower():
        return ord(input_string)-96
    else:
        return ord(input_string)-38

def determine_string_intersection(pockets: List[str]) -> str:
    for i in range(len(pockets)):
        if i == 0:
            intermediate_result = pockets[i]
        else:
            intermediate_result = set(intermediate_result).intersection(pockets[i])
    return intermediate_result.pop()

def transform_input(raw_puzzle_in: str) -> List[Any]:
    return raw_puzzle_in.split("\n")


def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    all_priorities = []

    for rucksacks in puzzle:
        rucksack_pockets = split_rucksack(rucksacks)
        intersection_string = determine_string_intersection(pockets=rucksack_pockets)
        priority = determine_priority(input_string=intersection_string)
        all_priorities.append(priority)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{sum(all_priorities)}") # 157 / 8176
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:

    def chunk_elves_into_groups(puzzle_input, no_in_groups = 3):
        return [puzzle_input[x:x+no_in_groups] for x in range(0, len(puzzle_input), no_in_groups)]

    puzzle = deepcopy(puzzle_in)

    all_priorities = []

    grouped_elves = chunk_elves_into_groups(puzzle)
    for group in grouped_elves:
        intersection_string = determine_string_intersection(pockets=group)
        priority = determine_priority(input_string=intersection_string)
        all_priorities.append(priority)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{sum(all_priorities)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input(aoc_input)
    solve_puzzle_2(transfrmd_inp_p2)
