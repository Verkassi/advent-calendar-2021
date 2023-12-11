from copy import deepcopy
from pathlib import Path
import itertools
from typing import List

def read_input(is_test: bool = False):
    if is_test:
        input_file = Path("inputs/test.txt")
    else:
        input_file = Path("inputs/actual.txt")

    with open(input_file) as file:
        content = file.read().splitlines()
    return content


def convert_input_to_grid_with_size(puzzle_rows: list[str]):
    puzzle_grid = list([ [ char for char in row ] for row in puzzle_rows ])
    max_lenght = len(puzzle_grid)-1 # Corrected for index
    max_width = len(puzzle_grid[0])-1 # Corrected for index
    return (puzzle_grid, max_lenght, max_width)

def determine_valid_surroundings(
        current_horizontal_positions: list[int],
        max_horizontal_position: str,
        current_vertical_position: list[int],
        max_vertical_position: str
):
    def _determine_valid_steps(current_pos: list[int], max_pos):
        possible_pos = list()
        if current_pos[0] > 0:
            possible_pos.append(current_pos[0]-1)
        if current_pos[-1] < max_pos:
            possible_pos.append(current_pos[-1]+1)
        return possible_pos

    horizontal_checks = _determine_valid_steps(current_pos=current_horizontal_positions, max_pos=max_horizontal_position)
    vertical_checks = _determine_valid_steps(current_pos=[current_vertical_position], max_pos=max_vertical_position)

    horizontals = list(itertools.product(horizontal_checks,[current_vertical_position]))
    verticals = list(itertools.product(current_horizontal_positions,vertical_checks))
    diagonals = list(itertools.product(horizontal_checks,vertical_checks))
    return horizontals + verticals + diagonals

def determine_complete_digit_with_positions(current_horizontal_position: int, current_row: List[str]):
    number_sequence = list()
    number_position_sequence = list()
    remainder_of_row = current_row[current_horizontal_position:]

    for item in remainder_of_row:
        if item.isdigit():
            number_sequence.append(current_row[current_horizontal_position])
            number_position_sequence.append(current_horizontal_position)
        else:
            break
        current_horizontal_position += 1

    return (int(''.join(number_sequence)), number_position_sequence)

def has_surrounding_symbol(positions_to_check: list[tuple], puzzle_grid: list[list[str]]):
    false_positives = {'0','1','2','3','4','5','6','7','8','9','.'}

    surrounding_symbols = set()
    for position_to_check in positions_to_check:
        surrounding_symbols.add(puzzle_grid[position_to_check[1]][position_to_check[0]])
    
    return (surrounding_symbols - false_positives) == set()

def find_gear_ratio(puzzle_grid: list[list[str]], positions_to_check: list[tuple]):
    row_pos = 0
    for position_to_check in positions_to_check:
        if puzzle_grid[position_to_check[1]][position_to_check[0]].isdigit():
            print(f"isdigit: {puzzle_grid[position_to_check[1]][position_to_check[0]]}")
            # Write function that checks the row of the digit found to the left and right for the whole number

def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    # Convert engine schematic to a grid
    puzzle_grid, max_lenght, max_width = convert_input_to_grid_with_size(puzzle_rows=puzzle)

    # results
    with_surrounding_symbol = list()
    without_surrounding_symbol = list()

    for i, row in enumerate(puzzle_grid):
        row_pos = 0
        while row_pos <= max_width:
            field_value = row[row_pos]
            # if column is a number
            if field_value.isdigit():
                current_number, number_horizontal_positions = determine_complete_digit_with_positions(current_horizontal_position=row_pos, current_row=row)
                possible_checks = determine_valid_surroundings(
                    current_horizontal_positions=number_horizontal_positions,
                    max_horizontal_position=max_width,
                    current_vertical_position=i,
                    max_vertical_position=max_lenght
                )
                if has_surrounding_symbol(positions_to_check=possible_checks, puzzle_grid=puzzle_grid):
                    with_surrounding_symbol.append(current_number)
                else:
                    without_surrounding_symbol.append(current_number)
                row_increment = len(number_horizontal_positions)
            else:
                row_increment = 1
            row_pos += row_increment

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(sum(without_surrounding_symbol))
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    # Convert engine schematic to a grid
    puzzle_grid, max_lenght, max_width = convert_input_to_grid_with_size(puzzle_rows=puzzle)

    # results
    with_surrounding_symbol = list()
    without_surrounding_symbol = list()

    for i, row in enumerate(puzzle_grid):
        row_pos = 0
        while row_pos <= max_width:
            field_value = row[row_pos]
            # if column is a number
            if field_value == '*':
                possible_checks = determine_valid_surroundings(
                    current_horizontal_positions=[row_pos],
                    max_horizontal_position=max_width,
                    current_vertical_position=i,
                    max_vertical_position=max_lenght
                )
                gear_ratio = find_gear_ratio(
                    puzzle_grid=puzzle_grid,
                    positions_to_check=possible_checks
                )
            row_pos += 1

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{puzzle}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = read_input(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = read_input(is_test=True)
    solve_puzzle_2(transfrmd_inp_p2)
