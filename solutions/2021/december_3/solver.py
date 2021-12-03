from puzzle_input import aoc_input, tst_input
import collections

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
    transposed_list=list(map(list, zip(*in_list)))
    gamma_rate_bn_lst=[]
    epsilon_rate_bn_lst=[]

    for i in range(len(transposed_list)):
        counter=collections.Counter(transposed_list[i])
        gamma_rate_bn_lst.append(counter.most_common(1)[0][0])
        epsilon_rate_bn_lst.append(counter.most_common()[1][0])

    gamma_rate = int("".join(gamma_rate_bn_lst), 2)
    epsilon_rate = int("".join(epsilon_rate_bn_lst), 2)
    power = gamma_rate*epsilon_rate
    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Gamma: {gamma_rate}, Epsilon: {epsilon_rate}, Power: {power}")
    print("-----------------------------------------------------")


def solve_puzzle_2(in_list: list) -> None:
    # Puzzle logic:
    # 
    # Answer:
    # 

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    solve_puzzle_1(aoc_input)
    solve_puzzle_2(tst_input)
