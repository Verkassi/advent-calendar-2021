from collections import Counter
from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    rows = raw_puzzle_in.splitlines()
    cal_per_elf = []
    all_elfs_with_cals = []
    for row in rows:
        if row != "":
            cal_per_elf.append(int(row))
        else:
            all_elfs_with_cals.append(cal_per_elf)
            cal_per_elf = []
    all_elfs_with_cals.append(cal_per_elf)

    return all_elfs_with_cals


def solve_puzzle_1(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)

    most_cal_elf = 0
    cur_max_cal = 0
    cur_elf = 0
    for elf in puzzle:
        cur_elf += 1
        if (cur_cal := sum(elf)) >= cur_max_cal:
            cur_max_cal = cur_cal
            most_cal_elf = cur_elf

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{most_cal_elf} with {cur_max_cal} calories!")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)
    elves_with_cals = dict()

    start_elf = 1
    for elf in puzzle:
        elves_with_cals[start_elf] = sum(elf)
        start_elf += 1

    elves_counter = Counter(elves_with_cals)
    highest_cals = elves_counter.most_common(3)

    top_three_cals = sum(i[1] for i in highest_cals)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{top_three_cals}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp)
    solve_puzzle_2(transfrmd_inp)
