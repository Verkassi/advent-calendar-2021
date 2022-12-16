from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    puzzle_segments = raw_puzzle_in.split("\n\n")

    # Stack
    original_stack = puzzle_segments[0]
    original_stack = original_stack.split("\n")
    stack_numbers = original_stack.pop()
    stack_numbers = stack_numbers.strip()
    highest_stack_number = stack_numbers[-1]

    # every row is 3 stack chars and one space
    row_transpone = dict()
    for row in range(int(highest_stack_number)):
        current_stack = []
        for boxes in original_stack:
            starting_point = row + (row * 3)
            print(boxes[starting_point : starting_point + 3])
            current_stack.append(boxes[starting_point : starting_point + 3])
        row_transpone[row + 1] = current_stack

    # Movements
    movements = puzzle_segments[1]
    movements = movements.splitlines()
    # Int 1 == number of items
    # Int 2 == From
    # Int 3 == To

    return [row_transpone, movements]


def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{puzzle}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{puzzle}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(tst_input)
    solve_puzzle_1(transfrmd_inp_p1)
    # transfrmd_inp_p2 = transform_input(tst_input)
    # solve_puzzle_2(transfrmd_inp_p2)
