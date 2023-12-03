from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input


TRANSLATIONS = {
    "A": {
        "translation": "rock",
        "points": 1
    },
    "X": {
        "translation": "rock",
        "points": 1
    },
    "B": {
        "translation": "paper",
        "points": 2
    },
    "Y": {
        "translation": "paper",
        "points": 2
    },
    "C": {
        "translation": "scissors",
        "points": 3
    },
    "Z": {
        "translation": "scissors",
        "points": 3
    },
}
ROUND_POINTS = {
    "lose": 0,
    "draw": 3,
    "win": 6
}
XYZ_TO_RESULTS = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}


def transform_input(raw_puzzle_in: str) -> List[Any]:
    strategy_rows = raw_puzzle_in.split("\n")
    strategy_table = []
    for row in strategy_rows:
        strategy_table.append(row.split(" "))

    return strategy_table


def determine_outcome(elf_pick, my_pick) -> str:
    # Convert input
    elf_input = TRANSLATIONS[elf_pick]["translation"]
    my_input = TRANSLATIONS[my_pick]["translation"]

    if my_input == elf_input:
        return "draw"
    elif any(
        [
            (my_input == "rock" and elf_input == "scissors"),
            (my_input == "paper" and elf_input == "rock"),
            (my_input == "scissors" and elf_input == "paper")
        ]
    ):
        return "win"
    elif any(
        [
            (my_input == "scissors" and elf_input == "rock"),
            (my_input == "rock" and elf_input == "paper"),
            (my_input == "paper" and elf_input == "scissors")
        ]
    ):
        return "lose"
    else:
        raise ValueError("COULD NOT COMPUTE OUTPUT")


def calc_outcome_points(outcome, my_input) -> int:
    return ROUND_POINTS[outcome] + TRANSLATIONS[my_input]["points"]


def translate_pick(elf_pick, expected_result) -> str:
    RESULT_TRANSLATION = {
        "rock": {
            "win": "paper",
            "lose": "scissors"
        },
        "paper": {
            "win": "scissors",
            "lose": "rock"
        },
        "scissors": {
            "win": "rock",
            "lose": "paper"
        }
    }
    expected_result_translated = XYZ_TO_RESULTS[expected_result]
    elf_input = TRANSLATIONS[elf_pick]["translation"]

    if expected_result_translated == "draw":
        return elf_input
    else:
        result = RESULT_TRANSLATION[elf_input][expected_result_translated]
        return result


def solve_puzzle_1(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)

    round_points = []
    for round in puzzle:
        outcome = determine_outcome(elf_pick=round[0], my_pick=round[1])
        round_points.append(calc_outcome_points(
            outcome=outcome, my_input=round[1]))

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{sum(round_points)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)

    backwards_translate_my_pick = {
        "rock": "X",
        "paper": "Y",
        "scissors": "Z",
    }

    round_points = []
    for round in puzzle:
        my_pick = translate_pick(elf_pick=round[0], expected_result=round[1])
        my_pick = backwards_translate_my_pick[my_pick]
        # Translation works
        outcome = XYZ_TO_RESULTS[round[1]]
        round_points.append(
            calc_outcome_points(outcome=outcome, my_input=my_pick)
        )

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{sum(round_points)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp)
    solve_puzzle_2(transfrmd_inp)
