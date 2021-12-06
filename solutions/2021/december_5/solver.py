from copy import deepcopy

from puzzle_input import aoc_input, tst_input


def transform_input(raw_puzzle_in: str):
    # Format: x1,y1 -> x2,y2
    output = []
    rows = raw_puzzle_in.replace(" ", "").splitlines()
    for row in rows:
        row = row.split("->")
        tmp_row = []
        for entry in row:
            entry = entry.split(",")
            entry = tuple(int(item) for item in entry)
            tmp_row.append(entry)
        output.append(tmp_row)
    return output


def create_base_grid(grid_size: int = 10):
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(0)
        grid.append(row)
    return grid


def count_grid_numbers_higher(grid, gt_nr=2):
    rtrn_cnt = 0
    for row in grid:
        for col in row:
            if col >= gt_nr:
                rtrn_cnt += 1
    return rtrn_cnt


def solve_puzzle_1(puzzle_in, base_grid) -> None:
    # Puzzle logic:
    # Consider where x1 = x2 and y1 = y2
    # Grid is 0,0 to 9,9
    # Answer:
    #

    # slope = (y1-y2)/(x1-x2)
    grid = deepcopy(base_grid)

    for entry in puzzle_in:
        x_coords = sorted([entry[0][0], entry[1][0]])
        y_coords = sorted([entry[0][1], entry[1][1]])
        if x_coords[0] == x_coords[1]:
            for i in range(y_coords[0], y_coords[1] + 1):
                grid[i][x_coords[0]] += 1
        elif y_coords[0] == y_coords[1]:
            for i in range(x_coords[0], x_coords[1] + 1):
                grid[y_coords[0]][i] += 1

    nrs_higher_than_2 = count_grid_numbers_higher(grid, 2)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of double overlaps: {nrs_higher_than_2}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in, base_grid) -> None:
    # Puzzle logic:
    #
    # Answer:
    #
    grid = deepcopy(base_grid)

    for entry in puzzle_in:
        x_coords = (entry[0][0], entry[1][0])
        y_coords = (entry[0][1], entry[1][1])
        x_coords_srt = sorted(x_coords)
        y_coords_srt = sorted(y_coords)
        if x_coords_srt[0] == x_coords_srt[1]:
            for i in range(y_coords_srt[0], y_coords_srt[1] + 1):
                grid[i][x_coords_srt[0]] += 1
        elif y_coords_srt[0] == y_coords_srt[1]:
            for i in range(x_coords_srt[0], x_coords_srt[1] + 1):
                grid[y_coords_srt[0]][i] += 1
        else:
            # x1,y1 -> x2,y2 ==> x1,x2 | y1,y2
            # 8,0 -> 0,8 ==> 8,0 | 0,8 // Moves from right to left
            # 0,0 -> 8,8 ==> 0,8 | 0,8 // Moves from left to right
            # 0,9 -> 2,9 ==> 0,2 | 9,9

            number_of_steps = 0
            for i in range(x_coords_srt[0], x_coords_srt[1] + 1):
                number_of_steps += 1

            x_entries = [
                i for i in range(x_coords_srt[0], x_coords_srt[1] + 1)
            ]
            if x_coords[0] > x_coords[1]:
                x_entries.reverse()

            y_entries = [
                i for i in range(y_coords_srt[0], y_coords_srt[1] + 1)
            ]
            if y_coords[0] > y_coords[1]:
                y_entries.reverse()

            for i in range(number_of_steps):
                grid[y_entries[i]][x_entries[i]] += 1

    nrs_higher_than_2 = count_grid_numbers_higher(grid, 2)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"Number of double overlaps: {nrs_higher_than_2}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp = transform_input(aoc_input)
    solve_puzzle_1(transfrmd_inp, create_base_grid(grid_size=1000))
    solve_puzzle_2(transfrmd_inp, create_base_grid(grid_size=1000))
