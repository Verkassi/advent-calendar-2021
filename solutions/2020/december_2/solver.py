from typing import List

from puzzle_input import aoc_input, tst_input


def solve_puzzle_1(in_list: list) -> None:
    # Find two entries that add up to 2020
    # Puzzle logic:
    # 1-3 a: abcde <- between 1 and 3 a's
    # 1-3 b: cdefg <- between 1 and 3 b's
    # 2-9 c: ccccccccc <- between 2 and 9 c's
    # Answer:
    # 2 are valid, second entry is invalid
    valids = 0
    invalids = 0
    for entry in in_list:
        appart = entry.split(
            " "
        )  # Split text into three segments: entries, letter and password
        entries = appart[0].split("-")
        min_entry = int(entries[0])  # Get the minimal number of occurances
        max_entry = int(entries[1])  # Get the maximal number of occurances
        search_character = appart[1].replace(
            ":", ""
        )  # Get the character to look for
        pwd = appart[2]  # Password string
        list_of_chars: List[str] = []
        list_of_chars[:0] = pwd  # Split the password characters into an array
        char_occurances = list_of_chars.count(search_character)
        if min_entry <= char_occurances <= max_entry:
            valids += 1
        else:
            invalids += 1

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of passwords: {len(in_list)}")
    print(f"Number of invalid passwords: {invalids}")
    print(f"Number of valid passwords: {valids}")
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Find three entries that add up to 2020
    # Puzzle logic:
    # 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    # 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    # 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    # Answer:
    # Number of valids = 1
    valids = 0
    invalids = 0
    for entry in in_list:
        appart = entry.split(
            " "
        )  # Split text into three segments: entries, letter and password
        entries = appart[0].split("-")
        entry_position_one = (
            int(entries[0]) - 1
        )  # Get the minimal number of occurances
        entry_position_two = (
            int(entries[1]) - 1
        )  # Get the maximal number of occurances
        search_character = appart[1].replace(
            ":", ""
        )  # Get the character to look for
        pwd = appart[2]  # Password string
        list_of_chars: List[str] = []
        list_of_chars[:0] = pwd  # Split the password characters into an array
        try:
            first_result = (
                search_character == list_of_chars[entry_position_one]
            )
        except:
            first_result = False
        try:
            second_result = (
                search_character == list_of_chars[entry_position_two]
            )
        except:
            second_result = False

        # Check if only one matches
        if first_result:
            if not second_result:
                valids += 1
            else:
                invalids += 1
        else:
            if second_result:
                valids += 1
            else:
                invalids += 1

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Number of passwords: {len(in_list)}")
    print(f"Number of invalid passwords: {invalids}")
    print(f"Number of valid passwords: {valids}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(aoc_input)
    solve_puzzle_2(aoc_input)
