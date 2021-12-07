import collections
from typing import Any, Tuple

from puzzle_input import aoc_input, tst_input


def solve_puzzle_1(in_list: list) -> None:
    # Puzzle logic:
    # 00100
    # 11110
    # 10110
    # 10111
    # 10101
    # 01111
    # 00111
    # 11100
    # 10000
    # 11001
    # 00010
    # 01010
    # Answer:
    #   Gamma:      10110 -> 22
    #   Epsilon:    01001 -> 9
    #   power:      22 * 9 = 198
    transposed_list = list(map(list, zip(*in_list)))
    gamma_rate_bn_lst = []
    epsilon_rate_bn_lst = []

    for i in range(len(transposed_list)):
        counter = collections.Counter(transposed_list[i])
        gamma_rate_bn_lst.append(counter.most_common(1)[0][0])
        epsilon_rate_bn_lst.append(counter.most_common()[1][0])

    gamma_rate = int("".join(gamma_rate_bn_lst), 2)
    epsilon_rate = int("".join(epsilon_rate_bn_lst), 2)
    power = gamma_rate * epsilon_rate
    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Gamma: {gamma_rate}, Epsilon: {epsilon_rate}, Power: {power}")
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Puzzle logic:
    # Flow:
    # Start with full list from diagnostic report
    # Consider just the first bit of each row
    # Keep only numbers from the bit criteria:
    #   ox_gen_rating = most common value in current bit position, if equals keep 1
    #   co2_scrub_rating = least common value, if equals keep 0
    # If there is only one number left, stop; this is the rating value
    # Answer:
    # Oxygen: 23
    # CO2: 10
    # LSR: 230

    def find_commons(inputlist: list) -> Tuple[Any, Any]:
        counter = collections.Counter(inputlist)
        commons = counter.most_common()
        # Check if entries are equal
        if commons[0][1] == commons[1][1]:
            return ("equal", None)
        else:
            return (commons[0][0], commons[1][0])

    def calc_matching_bitstring(
        input_list: list, equals_handler: str, calc_type: str
    ) -> str:
        row_width = len(input_list[0])
        tmp_in_list = input_list

        for y in range(row_width):
            if len(tmp_in_list) == 1:
                break
            transposed_list = list(map(list, zip(*tmp_in_list)))
            high_cur_mc, low_cur_mc = find_commons(transposed_list[y])
            # handle equals per case
            if high_cur_mc == "equal":
                cur_mc = equals_handler
            else:
                if calc_type == "oxy":
                    cur_mc = high_cur_mc
                else:
                    cur_mc = low_cur_mc
            tmp_in_list = [
                tmp_in_list[idx]
                for idx, entry in enumerate(tmp_in_list)
                if entry[y] == cur_mc
            ]
        return tmp_in_list[0]

    oxygen_generator_rating = int(
        calc_matching_bitstring(in_list, "1", calc_type="oxy"), 2
    )
    co2_scrubber_rating = int(
        calc_matching_bitstring(in_list, "0", calc_type="co2"), 2
    )
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(
        f"Oxygen: {oxygen_generator_rating}, CO2: {co2_scrubber_rating}, Life Support Rate: {life_support_rating}"
    )
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(aoc_input)
    solve_puzzle_2(aoc_input)
