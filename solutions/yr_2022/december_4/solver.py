from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    puzzle_input = raw_puzzle_in.split("\n")
    extracted_puzzle_input = []
    for pair in puzzle_input:
        converted_pair = []
        for elf in pair.split(","):
            elf_range = elf.split("-")
            elf_sections = set(i for i in range(int(elf_range[0]), int(elf_range[1]) + 1))
            converted_pair.append(elf_sections)
        extracted_puzzle_input.append(converted_pair)
    return extracted_puzzle_input


def print_overlaps(puzzle):
    for pair in puzzle:
        for elf in pair:
            base_print = [".", ".", ".", ".", ".", ".", ".", ".", "."]
            for section in elf:
                base_print[section - 1] = str(section)
            print("".join(base_print))
        print("\n")


def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    # print_overlaps(puzzle=puzzle)

    no_full_overlaps = 0
    for pair in puzzle:
        section_elf_one = pair[0]
        section_elf_two = pair[1]
        all_two_in_one = section_elf_one - section_elf_two
        all_one_in_two = section_elf_two - section_elf_one
        if all_one_in_two == set() or all_two_in_one == set():
            no_full_overlaps += 1

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{no_full_overlaps}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    no_overlaps = 0
    for pair in puzzle:
        section_elf_one = pair[0]
        section_elf_two = pair[1]
        if set() != section_elf_one.intersection(section_elf_two):
            no_overlaps += 1

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{no_overlaps}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input(aoc_input)
    solve_puzzle_2(transfrmd_inp_p2)
