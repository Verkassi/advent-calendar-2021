from copy import deepcopy
from typing import Any, List

from puzzle_input import aoc_input, tst_input, larger_tst_input, tst_single, ref_set


def transform_input(raw_puzzle_in: str) -> List[Any]:
    lines = raw_puzzle_in.splitlines()

    puzzle_return = []
    for line in lines:
        input_helper = line.split(" | ")[0].split(" ")
        output_helper = line.split(" | ")[1].split(" ")

        input_list = []
        for entry in input_helper:
            tmp_lst = []
            tmp_lst[:0] = entry
            input_list.append(set(tmp_lst))

        output_list = []
        for entry in output_helper:
            tmp_lst = []
            tmp_lst[:0] = entry
            output_list.append(set(tmp_lst))

        puzzle_return.append([input_list, output_list])

    return puzzle_return


def solve_puzzle_1(puzzle_in: list) -> None:
    # Puzzle logic:
    #   Number Shape:
    #     aaaa
    #    b    C
    #    b    c
    #     dddd
    #    e    f
    #    e    f
    #     gggg
    #   Puzzle faces:
    #   - 0 : 6 | Overlaps with: 8
    #   - 1 : 2 | Overlaps with: 0, 3, 4, 7, 8, 9
    #   - 2 : 5 | Overlaps with: 8
    #   - 3 : 5 | Overlaps with: 8, 9
    #   - 4 : 4 | Overlaps with: 8, 9
    #   - 5 : 5 | Overlaps with: 6, 8
    #   - 6 : 6 | Overlaps with: 8
    #   - 7 : 3 | Overlaps with: 0, 3, 8, 9
    #   - 8 : 7 | Overlaps with: None
    #   - 9 : 6 | Overlaps with: 8
    # Answer:
    #

    puzzle = deepcopy(puzzle_in)

    unique_lengths = 0

    for row in puzzle:
        for output in row[1]:  # Only take outputs
            if len(output) in [2, 3, 4, 7]:
                unique_lengths += 1

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of unique numbers on display: {unique_lengths}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    # Puzzle logic:
    #
    # Answer:
    #

    def decode_line(single_slice_smp, single_slice_out):
        tmp_dict = {}

        # First lengths we know
        easy_guess = [entry for entry in single_slice_smp if len(entry) in [2, 3, 4, 7]]
        for guess in easy_guess:
            no_chars = len(guess)
            if no_chars == 2:
                tmp_dict["1"] = guess
            elif no_chars == 3:
                tmp_dict["7"] = guess
            elif no_chars == 4:
                tmp_dict["4"] = guess
            elif no_chars == 7:
                tmp_dict["8"] = guess

        # Then the fivers
        five_guess = [entry for entry in single_slice_smp if len(entry) == 5]
        for guess in five_guess:
            if len(tmp_dict["8"] - tmp_dict["1"] - guess) == 2:
                tmp_dict["3"] = guess
            elif len(tmp_dict["8"] - tmp_dict["7"] - tmp_dict["4"] - guess) == 1:
                tmp_dict["5"] = guess
            elif len(tmp_dict["8"] - tmp_dict["7"] - tmp_dict["4"] - guess) == 0:
                tmp_dict["2"] = guess
            else:
                raise ValueError(f"COULD NOT DECODE FIVE GUESS: {guess}")

        # Then the length six, for which we can do subtractions
        six_guess = [entry for entry in single_slice_smp if len(entry) == 6]
        for guess in six_guess:
            sub_set = tmp_dict["8"] - tmp_dict["7"]
            sub_sub_set = sub_set - tmp_dict["4"]
            # Find 6 -> 8 - 7 - 6 = 0 (c)
            if len(tmp_dict["8"] - tmp_dict["7"] - guess) == 0:
                tmp_dict["6"] = guess
            # Find 9 -> 8 - 7 - 4 - 9 = 1 (e)
            elif len(tmp_dict["8"] - tmp_dict["7"] - tmp_dict["4"] - guess) == 1:
                tmp_dict["9"] = guess
            # Find 0 -> 8 - 7 - 4 - 0 = 1 (d)
            elif len(tmp_dict["8"] - tmp_dict["7"] - tmp_dict["4"] - guess) == 0:
                tmp_dict["0"] = guess
            else:
                raise ValueError(f"COULD NOT DECODE SIX GUESS: {guess}") 

        match_dict = {}
        for k,v in tmp_dict.items():
            # print(k,"".join(v))
            match_dict[("".join(sorted(v)))] = k

        return int("".join([match_dict["".join(sorted(entry))] for entry in single_slice_out]))

    puzzle = deepcopy(puzzle_in)

    answers = []
    for i, line in enumerate(puzzle):
        # print(i+1)
        decoded_dict = decode_line(single_slice_smp=line[0], single_slice_out=line[1])
        # print(decoded_dict)
        answers.append(decoded_dict)

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"Sum of four-digit output values is: {sum(answers)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp)
    solve_puzzle_2(transfrmd_inp)
