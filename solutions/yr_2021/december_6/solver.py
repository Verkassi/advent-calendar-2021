from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str):
    return raw_puzzle_in


def solve_puzzle_1(puzzle_in: list) -> None:
    # Puzzle logic:
    # - Each lanternfish creates a new lanternfish every 7 days
    # - Not all births are on the same day (see test data)
    # - Array = NO days for new LF
    # - New lanternfish needs 2 days EXTRA to age and then start 7 days -> will be 8, since last count is 0
    # - Timer 0 = 7, after that start on 6
    # CALC FOR NO DAYS = 80
    # Answer:
    # 

    fishlist = puzzle_in

    print(fishlist)
    no_days = 80
    for day in range(1, no_days+1):
        no_fish = len(fishlist)
        for i in range(no_fish):
            if fishlist[i] == 0:
                fishlist[i] = 6
                fishlist.append(8)
            else:
                fishlist[i] -= 1

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of Fish: {len(fishlist)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(tst_input)
    solve_puzzle_1(transfrmd_inp)
    solve_puzzle_2(transfrmd_inp)
