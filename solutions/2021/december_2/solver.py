from puzzle_input import aoc_input, tst_input


def solve_puzzle_1(in_list: list) -> None:
    # Puzzle logic:
    # forward = + horizontal
    # down    = + depth
    # up      = - depth
    # Answer:
    # sum of depth and horizontal position = 150

    cur_depth = 0
    cur_horizontal = 0

    for row in in_list:
        row_sub = row.split(" ")
        text_part = row_sub[0]
        addition = int(row_sub[1])

        if text_part == "down":
            cur_depth = cur_depth + addition
        elif text_part == "up":
            addition = 0 - addition  # Make negative
            cur_depth = cur_depth + addition
        elif text_part == "forward":
            cur_horizontal = cur_horizontal + (addition)
        else:
            raise ValueError(f"Text is {text_part}, did't expect that")

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"depth: {cur_depth}, horizontal: {cur_horizontal}")
    print(f"Sum of depth and horizontal is: {cur_depth*cur_horizontal}")
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Puzzle logic:
    # forward = + horizontal | depth * aim
    # down    = + aim
    # up      = - aim
    # Answer:
    # sum of depth and horizontal position = 900

    cur_depth = 0
    cur_horizontal = 0
    cur_aim = 0

    for row in in_list:
        row_sub = row.split(" ")
        text_part = row_sub[0]
        addition = int(row_sub[1])

        if text_part == "down":
            cur_aim = cur_aim + addition
        elif text_part == "up":
            addition = 0 - addition  # Make negative
            cur_aim = cur_aim + addition
        elif text_part == "forward":
            cur_horizontal = cur_horizontal + (addition)
            cur_depth = cur_depth + (cur_aim * addition)
        else:
            raise ValueError(f"Text is {text_part}, did't expect that")

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"depth: {cur_depth}, horizontal: {cur_horizontal}, aim: {cur_aim}")
    print(f"Sum of depth and horizontal is: {cur_depth*cur_horizontal}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(tst_input)
    solve_puzzle_2(tst_input)
