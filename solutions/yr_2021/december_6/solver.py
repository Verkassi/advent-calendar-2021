from puzzle_input import aoc_input, tst_input
from copy import deepcopy
from time import time

def transform_input(raw_puzzle_in: str):
    return raw_puzzle_in


def calc_no_fish_after_days(fish_list: list, no_days: int, debug_print=False) -> int:
    try:
        start_time = time()
        lantern_fish_list = deepcopy(fish_list)

        fish_birth_cntr = {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
        }

        for input_fish in lantern_fish_list:
            fish_birth_cntr[str(input_fish)]+=1

        for day in range(no_days):
            birth_placeholder = fish_birth_cntr["0"]
            restart_placeholder = fish_birth_cntr["0"]
            fish_birth_cntr["0"] = fish_birth_cntr["1"]
            fish_birth_cntr["1"] = fish_birth_cntr["2"]
            fish_birth_cntr["2"] = fish_birth_cntr["3"]
            fish_birth_cntr["3"] = fish_birth_cntr["4"]
            fish_birth_cntr["4"] = fish_birth_cntr["5"]
            fish_birth_cntr["5"] = fish_birth_cntr["6"]
            fish_birth_cntr["6"] = fish_birth_cntr["7"] + restart_placeholder
            fish_birth_cntr["7"] = fish_birth_cntr["8"]
            fish_birth_cntr["8"] = birth_placeholder

        no_fish = 0
        for value in fish_birth_cntr.values():
            no_fish+=value
    finally:
        end_time = time()
        if debug_print:
            print(f"Operation took: {end_time-start_time} seconds.")

    return no_fish


def calc_fish_iterative(fish_list: list, no_days: int, debug_print=False) -> int:
    try:
        start_time = time()

        fishlist = deepcopy(fish_list)
        for day in range(1, no_days+1):
            no_fish = len(fishlist)
            for i in range(no_fish):
                if fishlist[i] == 0:
                    fishlist[i] = 6
                    fishlist.append(8)
                else:
                    fishlist[i] -= 1
            if debug_print:
                print(f"Currently on day: {day}")
    finally:
        end_time = time()
        if debug_print:
            print(f"Operation took: {end_time-start_time} seconds.")
    return len(fishlist)


def solve_puzzle_1(puzzle_in: list, no_days: int) -> None:
    # Puzzle logic:
    # - Each lanternfish creates a new lanternfish every 7 days
    # - Not all births are on the same day (see test data)
    # - Array = NO days for new LF
    # - New lanternfish needs 2 days EXTRA to age and then start 7 days -> will be 8, since last count is 0
    # - Timer 0 = 7, after that start on 6
    # CALC FOR NO DAYS = 80
    # Answer:
    # 5934

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of Fish: {calc_fish_iterative(puzzle_in, no_days)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list, no_days: int) -> None:
    # Puzzle logic:
    # - Each lanternfish creates a new lanternfish every 7 days
    # - Not all births are on the same day (see test data)
    # - Array = NO days for new LF
    # - New lanternfish needs 2 days EXTRA to age and then start 7 days -> will be 8, since last count is 0
    # - Timer 0 = 7, after that start on 6
    # CALC FOR NO DAYS = 80
    # Answer:
    # 5934

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Number of Fish: {calc_no_fish_after_days(puzzle_in, no_days, True)}")
    print("-----------------------------------------------------")


def solve_puzzle_2_recursive(puzzle_in: list, no_days: int) -> None:
    # Puzzle logic:
    # - Each lanternfish creates a new lanternfish every 7 days
    # - Not all births are on the same day (see test data)
    # - Array = NO days for new LF
    # - New lanternfish needs 2 days EXTRA to age and then start 7 days -> will be 8, since last count is 0
    # - Timer 0 = 7, after that start on 6
    # CALC FOR NO DAYS = 80
    # Answer:
    # 5934

    # ! Important: Run with care ~!

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Number of Fish: {calc_fish_iterative(puzzle_in, no_days, True)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp, 18)
    solve_puzzle_2(transfrmd_inp, 256)
