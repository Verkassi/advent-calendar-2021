from copy import deepcopy
from pathlib import Path
from math import prod

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

def convert_input_puzzle1(is_test: bool = False, split_lines: bool = True):
    input_data = read_input(is_test=is_test, split_lines=split_lines)

    convert_puzzle = list()
    for data in input_data:
        converted_row = list()
        for instance in data.split()[1:]:
            converted_row.append(int(instance))
        convert_puzzle.append(converted_row)
    
    races = list()
    for i in range(len(convert_puzzle[0])):
        races.append(
            {
                "time": convert_puzzle[0][i],
                "dinstance": convert_puzzle[1][i]
            }
        )

    return races

def convert_input_puzzle2(is_test: bool = False, split_lines: bool = True):
    input_data = read_input(is_test=is_test, split_lines=split_lines)

    convert_puzzle = list()
    for data in input_data:
        converted_row = list()
        for instance in data.split()[1:]:
            converted_row.append(instance)
        convert_puzzle.append(int("".join(converted_row)))

    race = {
        "time": convert_puzzle[0],
        "dinstance": convert_puzzle[1]
    }

    return race

def calculate_possible_press_times(race: dict):
    winning_distance = race["dinstance"]
    race_time = race["time"]

    # travel_distance = (time - press_duration) * press_duration
    valid_press_time = list()
    for press_duration in range(1, race_time): # Skipping 0 and the maximum press time
        distance_traveled = (race["time"] - press_duration) * press_duration
        if distance_traveled > winning_distance:
            valid_press_time.append(press_duration)

    return valid_press_time

def solve_puzzle_1(puzzle_in: list) -> None:
    ## Important facts
    # Goal: Go farther than the best distance in each race
    # Controls:
    #   - Hold button == charge boat
    #   - Release button == move boat
    # Longer hold => move faster
    # Button holding counts towards the race
    # Input data:
    #   - Time = time in ms that you can race
    #   - Distance = record distance in millimeters
    #   - Each column is one race
    # Starting speed == 0 mm/s
    # 1 ms pressed == 1 mm/s for the remaining duration of the race

    # Puzzle goal: Determine the number of ways you can beat the record in each race
    # Multiply the options for each race to get the answer

    puzzle = deepcopy(puzzle_in)

    valid_press_times = [ calculate_possible_press_times(race=race) for race in puzzle ]

    options_per_race = [ len(race) for race in valid_press_times ]

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{prod(options_per_race)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    valid_press_times = calculate_possible_press_times(race=puzzle)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{len(valid_press_times)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = convert_input_puzzle1(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = convert_input_puzzle2(is_test=False)
    solve_puzzle_2(transfrmd_inp_p2)
