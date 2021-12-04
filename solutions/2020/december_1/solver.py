from puzzle_input import aoc_input, tst_input


def solve_puzzle_1(in_list: list) -> None:
    # Find two entries that add up to 2020
    # Puzzle logic:
    # 1721 <-
    # 979
    # 366
    # 299 <-
    # 675
    # 1456
    # Answer:
    # 1721 * 299 = 514579
    for i in range(len(in_list)):
        cur_entry = in_list[i]
        for j in range(len(in_list)):
            matching_entry = in_list[j]
            if i == j:
                continue  # Don't add the same entries
            else:
                if sum([cur_entry, matching_entry]) == 2020:
                    break
        else:
            continue
        break

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(
        f"Entries {cur_entry} and {matching_entry} become 2020, multiplying them gives {cur_entry*matching_entry}"
    )
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
    # Answer:
    # 1721 * 299 = 514579
    for i in range(len(in_list)):
        cur_entry = in_list[i]
        for j in range(len(in_list)):
            first_matching_entry = in_list[j]
            for k in range(len(in_list)):
                second_matching_entry = in_list[k]
                if i == j or i == k or j == k:
                    continue  # Don't add the same entries
                else:
                    if (
                        sum(
                            [
                                cur_entry,
                                first_matching_entry,
                                second_matching_entry,
                            ]
                        )
                        == 2020
                    ):
                        break
            else:
                continue
            break
        else:
            continue
        break

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(
        f"Entries {cur_entry}, {first_matching_entry} and {second_matching_entry} become 2020, multiplying them gives {cur_entry*first_matching_entry*second_matching_entry}"
    )
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(aoc_input)
    solve_puzzle_2(aoc_input)
