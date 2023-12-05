from copy import deepcopy
from pathlib import Path
from typing import List
import re

def read_input(is_test: bool = False):
    if is_test:
        input_file = Path("inputs/test.txt")
    else:
        input_file = Path("inputs/actual.txt")

    with open(input_file) as file:
        content = file.readlines()
    return content


def convert_input(game_input: List[str]):
    def _get_game_number(game_line: str):
        game_with_grabs = game_line.split(':')
        return int(game_with_grabs[0].replace('Game ',''))

    def _split_grabs_to_subsets(game_line: str):
        game_with_grabs = game_line.split(':')
        return [ x.strip() for x in game_with_grabs[1].strip().split(';') ]

    def _split_grabs(grab_subsets: List[str]):
        new_grab_subsets = list()
        for grab_subset in grab_subsets:
            new_grab_subsets.append([ grab.strip() for grab in grab_subset.split(',') ])
        return new_grab_subsets

    def _convert_subset_of_grabs_to_countable(grab_subsets: List[List[str]]):
        converted_grab_subsets = list()
        for grab in grab_subsets:
            converted_grab = dict()
            for color_grab in grab:
                ammount_with_color = color_grab.split(' ')
                converted_grab[ammount_with_color[1]] = int(ammount_with_color[0])
            converted_grab_subsets.append(converted_grab)
        return converted_grab_subsets
    
    converted_games = dict()

    for line in game_input:
        game_number = _get_game_number(game_line=line)
        grab_subsets=_split_grabs_to_subsets(
            game_line=line
        )
        countable_grabs=_convert_subset_of_grabs_to_countable(
            grab_subsets=_split_grabs(
                grab_subsets=grab_subsets
            )
        )

        converted_games[game_number] = countable_grabs
    return converted_games

def calculate_possible_games(games: dict, bag_content: dict):
    possible_games = list()
    for game_number, grabs in games.items():
        is_possible = True
        for grab in grabs:
            for grabbed_color, amount in grab.items():
                if amount > bag_content[grabbed_color]:
                    is_possible = False
        if is_possible:
            possible_games.append(game_number)
    return possible_games

def calculate_fewest_required_per_game(games: dict):
    games_with_minimum_ammounts = dict()
    for game, grabs in games.items():
        minimals = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for grab in grabs:
            for color, ammount in grab.items():
                if ammount > minimals[color]:
                    minimals[color] = ammount
        games_with_minimum_ammounts[game] = minimals
    return games_with_minimum_ammounts

def calculate_power_per_game(games: dict):
    def multiply_list(any_list: list):
        result = 1
        for x in any_list:
            result = result * x
        return result

    games_with_power = dict()

    for game, ammounts in games.items():
        cube_power = multiply_list(any_list=list(ammounts.values()))
        games_with_power[game] = cube_power
    
    return games_with_power

def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)
    converted_games = convert_input(
        game_input=puzzle
    )

    bag_content = {
        "blue": 14,
        "red": 12,
        "green": 13
    }

    possible_games = calculate_possible_games(
        games=converted_games,
        bag_content=bag_content
    )

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Possible games: {possible_games}")
    print(f"Sum of possible games: {sum(possible_games)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)
    converted_games = convert_input(
        game_input=puzzle
    )

    fewest_per_game = calculate_fewest_required_per_game(
        games=converted_games
    )

    games_with_power = calculate_power_per_game(
        games=fewest_per_game
    )

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{sum(games_with_power.values())}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = read_input(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = read_input(is_test=False)
    solve_puzzle_2(transfrmd_inp_p2)
