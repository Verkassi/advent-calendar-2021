from typing import Any, List

from puzzle_input import aoc_input, tst_input
from copy import deepcopy

def transform_input(raw_puzzle_in: str) -> List[Any]:
    return [int(entry) for entry in raw_puzzle_in.split(",")]


def solve_puzzle_1(puzzle_in: list) -> None:
    # Puzzle logic:
    # - Crab submarines can only move horizontally
    # - Match all horizontal positions
    # - Use as little feul as possible
    # - Data represents their horizontal position
    # - 1 step is 1 feul
    # - Short explanation: What is the smallest difference to get all numbers the same
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)

    diff_dict = {}
    for i in range(min(puzzle), max(puzzle)+1):
        tmp_difference = []
        for crab in puzzle:
            tmp_difference.append(abs(crab-i))
        diff_dict[str(i)] = sum(tmp_difference)

    smallest_diff = min(diff_dict, key=diff_dict.get) 

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Smallest difference is: {smallest_diff}, wich takes {diff_dict[smallest_diff]} fuel")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # Puzzle logic:
    # - Crab submarines can only move horizontally
    # - Match all horizontal positions
    # - Use as little feul as possible
    # - Data represents their horizontal position
    # - First step takes 1 fuel, second step takes 2 fuel -> 2 steps is 3 fuel?
    # - Short explanation: What is the smallest difference to get all numbers the same
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)

    diff_dict = {}
    for i in range(min(puzzle), max(puzzle)+1):
        tmp_difference = []
        for crab in puzzle:
            pos_diff = abs(crab-i)
            total_cost = sum([ i for i in range(1, pos_diff+1)])
            tmp_difference.append(total_cost)
        diff_dict[str(i)] = sum(tmp_difference)

    smallest_diff = min(diff_dict, key=diff_dict.get) 

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Smallest difference is: {smallest_diff}, wich takes {diff_dict[smallest_diff]} fuel")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp)
    solve_puzzle_2(transfrmd_inp)
