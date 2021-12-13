## Heavy inspiration from: https://github.com/plan-x64/advent-of-code-2021/blob/main/advent/day09.py

from copy import deepcopy
from typing import Any, List
from collections import deque
import functools

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    rows = raw_puzzle_in.splitlines()

    return_variable = []
    for row in rows:
        return_variable.append([int(dpth_nr) for dpth_nr in row])

    return return_variable


def surrounding(input, x, y):
    vals = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in vals if 0 <= x_i < len(input) and 0 <= y_i < len(input[x])]

def is_min(input, x, y):
    for (x_i, y_i) in surrounding(input, x, y):
        if input[x][y] == 9 or input[x_i][y_i] < input[x][y]:
            return False
    return True

def find_mins(input):
    mins = []
    for row in range(len(input)):
        for column in range(len(input[row])):
            if is_min(input, row, column):
                mins.append((row, column))
    return mins

def find_basin(input, x, y):
    basin = []
    visited = set()
    queue = deque([(x,y)])
    
    while queue:
        (x_i, y_i) = queue.pop()

        if (x_i, y_i) in visited:
            continue
        else:
            visited.add((x_i, y_i))
            if input[x_i][y_i] != 9:
                basin.append((x_i, y_i))
                queue.extend([(x_j, y_j) for (x_j, y_j) in surrounding(input, x_i, y_i) if (x_j, y_j) not in visited])
    return basin

def solve_puzzle_1(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)
    mins = find_mins(puzzle)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Part1: {sum([puzzle[x][y]+1 for (x,y) in mins])}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)
    mins = find_mins(puzzle)
    basins = [find_basin(puzzle, x, y) for (x, y) in mins]

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Part2: {functools.reduce(lambda a,b: a*b, sorted([len(basin) for basin in basins], reverse=True)[0:3])}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp)
    solve_puzzle_2(transfrmd_inp)
