from copy import deepcopy
from typing import Any, List
import re
from word2number import w2n

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    return raw_puzzle_in.split("\n")


def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    calibration_value = list()

    for line in puzzle:
        digits = re.findall(r'\d', line)
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        two_digit_number = first_digit * 10 + last_digit
        calibration_value.append(two_digit_number)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    # print(f"Found collaborations: {calibration_value}")
    print(f"Sum of all: {sum(calibration_value)}")
    print("-----------------------------------------------------")

def transform_input2(raw_puzzle_in: str) -> List[Any]:
    raw_puzzle_in = (
        raw_puzzle_in.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    return raw_puzzle_in.split("\n")

def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    calibration_value = list()

    for line in puzzle:
        digits = re.findall(r'\d', line)
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        two_digit_number = first_digit * 10 + last_digit
        calibration_value.append(two_digit_number)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    # print(f"Found collaborations: {calibration_value}")
    print(f"Sum of all: {sum(calibration_value)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input2(aoc_input)
    solve_puzzle_2(transfrmd_inp_p2)
