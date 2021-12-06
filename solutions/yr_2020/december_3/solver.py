import math
from typing import List

from puzzle_input import aoc_input, tst_input


def traverse_slope(in_list: list, x_step: int, y_step: int):
    no_trees = 0
    no_opens = 0
    iter_list = [item for idx, item in enumerate(in_list) if idx % y_step == 0]
    for i in range(len(iter_list)):
        if i > 0:
            current_row_pos = x_step * i
            pos_in_index = current_row_pos % len(iter_list[i])
            row_list = []
            row_list[:0] = iter_list[i]
            if row_list[pos_in_index] == ".":
                no_opens += 1
            else:
                no_trees += 1

    return (no_trees, no_opens)


def solve_puzzle_1(in_list: list) -> None:
    # Find two entries that add up to 2020
    # Puzzle logic:
    # 0)  S.##.........##.........##.........##.........##.........##.......  --->
    # 1)  #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    # 2)  .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    # 3)  ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    # 4)  .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    # 5)  ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    # 6)  .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    # 7)  .#........#.#........X.#........#.#........#.#........#.#........#
    # 8)  #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    # 9)  #...##....##...##....##...#X....##...##....##...##....##...##....#
    # 10) .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
    # Answer:
    # S = start,
    # O = open,
    # X = tree
    # You encounter 7 trees

    (no_trees, no_opens) = traverse_slope(in_list, 3, 1)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of open trees: {no_trees}, number of opens: {no_opens}")
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Find three entries that add up to 2020
    # Puzzle logic:
    # Right 1, down 1. -> 2 trees
    # Right 3, down 1. -> 7 trees
    # Right 5, down 1. -> 3 trees
    # Right 7, down 1. -> 4 trees
    # Right 1, down 2. -> 2 trees
    # Answer:
    # 2*7*3*4*2 = 336

    x_y_combinations = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    result_tree_list = []
    result_open_list = []

    for combination in x_y_combinations:
        (no_trees, no_opens) = traverse_slope(
            in_list, combination[0], combination[1]
        )
        result_tree_list.append(no_trees)
        result_open_list.append(no_opens)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(
        f"Number of trees: {result_tree_list}, number of opens: {result_open_list}."
    )
    print(
        f"Product of all trees: {math.prod(result_tree_list)}, product of all opens: {math.prod(result_open_list)}"
    )
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(aoc_input)
    solve_puzzle_2(aoc_input)
