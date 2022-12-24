from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1
    return convert(raw_puzzle_in)

def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    ending_pos = 4

    for i in range(len(puzzle)):
        char_subset = puzzle[ending_pos-4:ending_pos]
        compare = list(set(char_subset))
        if sorted(char_subset) == sorted(compare):
            break
        else:
            ending_pos += 1


    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{ending_pos}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    ending_pos = 14
    offset = 14

    for i in range(len(puzzle)):
        char_subset = puzzle[ending_pos-offset:ending_pos]
        compare = list(set(char_subset))
        if sorted(char_subset) == sorted(compare):
            break
        else:
            ending_pos += 1

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{ending_pos}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input(aoc_input)
    solve_puzzle_2(transfrmd_inp_p2)
