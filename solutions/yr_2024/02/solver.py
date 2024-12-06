from copy import deepcopy
from pathlib import Path
from time import time

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
    # get the start time
    st = time()

    # Solve Puzzle
    puzzle = deepcopy(puzzle_in)

    reports = list()
    for row in puzzle:
        reports.append(list(map(int, row.split(" "))))

    safe = 0
    for i, report in enumerate(reports):
        print(f"Report {i}")
        # Two adjecent levels differ by at least 1 and at most three
        # Levels are either all increasing, or all decreasing
        for i, level in enumerate(report):
            # Prevent index error
            if i == len(report)-1:
                break
            else:
                level_difference = abs(report[i] - report[i+1])
            print(level_difference)
            if 0 < level_difference > 3:
                safe +=1
                break

    # get the end time
    et = time()

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(safe)
    print("------------------- RUN DURATION --------------------")
    print('Execution time:', round(st - et, 2), 'seconds')
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # get the start time
    st = time()

    # Solve Puzzle
    puzzle = deepcopy(puzzle_in)


    # get the end time
    et = time()

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(puzzle)
    print("------------------- RUN DURATION --------------------")
    print('Execution time:', round(st - et, 2), 'seconds')
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = convert_input(is_test=True)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = convert_input(is_test=True)
    solve_puzzle_2(transfrmd_inp_p2)
