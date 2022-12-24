from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str) -> List[Any]:
    puzzle_segments = raw_puzzle_in.split("\n\n")

    # Stack
    original_stack = puzzle_segments[0]
    original_stack = original_stack.split("\n")
    stack_numbers = original_stack.pop()
    stack_numbers = stack_numbers.strip()
    highest_stack_number = stack_numbers[-1]

    # every row is 3 stack chars and one space
    row_transpone = dict()
    for row in range(int(highest_stack_number)):
        current_stack = []
        for boxes in original_stack:
            starting_point = row + (row * 3)
            # print(boxes[starting_point : starting_point + 3])
            box = boxes[starting_point : starting_point + 3]
            if box != '   ':
                current_stack.append(box)
        current_stack.reverse()
        row_transpone[row + 1] = current_stack

    # Movements
    movements = puzzle_segments[1]
    movements = movements.splitlines()
    movement_lines = []
    for movement in movements:
        movement_separated = movement.split(" ")
        actual_movement = [int(movement_separated[1]), int(movement_separated[3]), int(movement_separated[5])]
        movement_lines.append(actual_movement)

    return [row_transpone, movement_lines]


def solve_puzzle_1(puzzle_in: list) -> None:
    stacks, movements = deepcopy(puzzle_in)

    for movement in movements:
        ammount = movement[0]
        from_stack = movement[1]
        to_stack = movement[2]
        for i in range(ammount):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)
    
    answer = []
    for k, v in stacks.items():
        answer.append(v.pop())

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{''.join(answer).replace('[','').replace(']','')}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    stacks, movements = deepcopy(puzzle_in)

    for movement in movements:
        # number of crates
        ammount = movement[0]

        # from to orientation
        from_stack = movement[1]
        to_stack = movement[2]

        # Moving
        stacks[to_stack] += stacks[from_stack][-ammount:]
        stacks[from_stack] = stacks[from_stack][:len(stacks[from_stack]) - ammount]

    top_crates = []
    for stack in stacks.values():
        if len(stack) >= 1:
            crate_value = f"{stack[-1].replace('[','').replace(']','')}"
            top_crates.append(crate_value)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{''.join(top_crates)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = transform_input(aoc_input)
    solve_puzzle_2(transfrmd_inp_p2)
