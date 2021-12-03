from typing import List

from puzzle_input import aoc_input, tst_input


def solve_puzzle_1(in_list: list) -> None:
    # Puzzle logic:
    # 199 (N/A - no previous measurement)
    # 200 (increased)
    # 208 (increased)
    # 210 (increased)
    # 200 (decreased)
    # 207 (increased)
    # 240 (increased)
    # 269 (increased)
    # 260 (decreased)
    # 263 (increased)
    # Answer:
    # increases = 7
    tot_equals = 0
    tot_increase = 0
    tot_decrease = 0
    for i in range(len(in_list)):
        cur_meas: int = in_list[i]
        if i == 0:
            None  # First entry knows no diff
        else:
            diff = cur_meas - prev_meas
            if diff == 0:
                tot_equals += 1
            elif diff > 0:
                tot_increase += 1
            elif diff < 0:
                tot_decrease += 1
            else:
                raise ValueError("Something is wrong dumdum!")
        prev_meas: int = cur_meas

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(
        f"increases: {tot_increase}, decreases: {tot_decrease}, equals: {tot_equals}"
    )
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Puzzle logic:
    # 199  A                  | A: 607 (N/A - no previous sum)
    # 200  A B                | B: 618 (increased)
    # 208  A B C              | C: 618 (no change)
    # 210    B C D            | D: 617 (decreased)
    # 200      C D E          | E: 647 (increased)
    # 207        D E F        | F: 716 (increased)
    # 240          E F G      | G: 769 (increased)
    # 269            F G H    | H: 792 (increased)
    # 260              G H    | I: BREAKS
    # 263                H    |
    # Answer:
    # increases = 5
    tot_increase = 0
    tot_decrease = 0
    tot_equals = 0
    for i in range(len(in_list)):
        if i >= (len(in_list) - 2):
            break  # Last entries cant be used to create a 3 wide window
        else:
            cur_meas: List[int] = [
                in_list[i],
                in_list[i + 1],
                in_list[i + 2],
            ]
            if i == 0:
                None  # First entry knows no diff
            else:
                diff = sum(cur_meas) - sum(prev_meas)
                if diff == 0:
                    tot_equals += 1
                elif diff > 0:
                    tot_increase += 1
                elif diff < 0:
                    tot_decrease += 1
                else:
                    raise ValueError("Something is wrong dumdum!")
        prev_meas: List[int] = cur_meas  # Save for next iteration
    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(
        f"increases: {tot_increase}, decreases: {tot_decrease}, equals: {tot_equals}"
    )
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(aoc_input)
    solve_puzzle_2(aoc_input)
