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

    # Get Puzzle Input
    puzzle = deepcopy(puzzle_in)

    list_1 = list()
    list_2 = list()
    # straighten out the lists
    for row in puzzle:
        splitted_row = row.split("   ")
        list_1.append(int(splitted_row[0]))
        list_2.append(int(splitted_row[1]))
    list_1.sort()
    list_2.sort()

    # Create sets of numbers
    matching_list = list()
    for i, item in enumerate(list_1):
        matching_list.append([list_1[i], list_2[i]])

    # Get answer
    total_distance = 0
    for item in matching_list:
        total_distance += abs((item[0] - item[1]))

    # get the end time
    et = time()

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(total_distance)
    print("------------------- RUN DURATION --------------------")
    print('Execution time:', round(st - et, 2), 'seconds')
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # get the start time
    st = time()

    # Solve Puzzle
    puzzle = deepcopy(puzzle_in)

    # straighten out the lists
    list_1 = list()
    list_2 = list()
    for row in puzzle:
        splitted_row = row.split("   ")
        list_1.append(int(splitted_row[0]))
        list_2.append(int(splitted_row[1]))
    list_1.sort()
    list_2.sort()

    # Count instances in list 2 per unique item in list 1
    total_counts_per_item = list()
    for item in list_1:
        occurances = list_2.count(item)
        total_counts_per_item.append(item*occurances)

    # get the end time
    et = time()

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(sum(total_counts_per_item))
    print("------------------- RUN DURATION --------------------")
    print('Execution time:', round(st - et, 2), 'seconds')
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = convert_input(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = convert_input(is_test=False)
    solve_puzzle_2(transfrmd_inp_p2)
