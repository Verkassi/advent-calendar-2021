from puzzle_input import aoc_input, tst_input


def solve_puzzle_1(in_list: list) -> None:
    # Find two entries that add up to 2020
    # Puzzle logic:
    # 1-3 a: abcde <- between 1 and 3 a's
    # 1-3 b: cdefg <- between 1 and 3 b's
    # 2-9 c: ccccccccc <- between 2 and 9 c's
    # Awnser: 2 are valid, second entry is invalid
    valids = 0
    invalids = 0
    for entry in in_list:
        appart = entry.split(" ", 0)
        min_entry = int(appart[0][1])
        max_entry = int(appart[0][-1])
        characters = appart[1].replace(":","")
        pwd = appart[2]
    list_of_chars = []
    list_of_chars[:0] = pwd
    ## Count number of password entries
    ## Validate if that number is in the range

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of passwords: {len(in_list)}")
    print(f"Number of invalid passwords: {valids}")
    print(f"Number of valid passwords: {invalids}")
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Find three entries that add up to 2020
    # Puzzle logic:
    # 1721
    # 979 <-
    # 366 <-
    # 299
    # 675 <-
    # 1456
    # Awnser = 1721 * 299 = 514579

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print()
    print("-----------------------------------------------------")


if __name__ == "__main__":
    # solve_puzzle_1(aoc_input)
    # solve_puzzle_2(aoc_input)
    pass
