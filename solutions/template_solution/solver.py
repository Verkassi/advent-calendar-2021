from copy import deepcopy
from pathlib import Path

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
    input_data = read_input(is_test=is_test, split_lines=split_lines)

    return input_data

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
    transfrmd_inp_p1 = convert_input(is_test=True)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = convert_input(is_test=True)
    solve_puzzle_2(transfrmd_inp_p2)
