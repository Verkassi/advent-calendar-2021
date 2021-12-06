from puzzle_input import aoc_input, tst_input
from copy import deepcopy
from itertools import chain

def transform_input(raw_puzzle_in: str):
    # Format: x1,y1 -> x2,y2
    output = []
    rows = raw_puzzle_in.replace(" ","").splitlines()
    for row in rows:
        row = row.split("->")
        tmp_row = []
        for entry in row:
            entry = entry.split(",")
            entry = tuple( int(item) for item in entry )
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



def solve_puzzle_1(puzzle_in, base_grid) -> None:
    # Puzzle logic:
    # Consider where x1 = x2 and y1 = y2
    # Grid is 0,0 to 9,9
    # Answer:
    #

    # slope = (y1-y2)/(x1-x2)
    grid = deepcopy(base_grid)

    # Calculate all steps
    grid_entries = []
    for entry in puzzle_in:
        x_coords, y_coords = zip(*entry) # Convert to format [(x1,x2), (y1,y2)]
        x_coords = sorted(x_coords)
        y_coords = sorted(y_coords)
        line = []
        if x_coords[0] == x_coords[1]:
            for i in range(y_coords[0], y_coords[1]+1):
                line.append((x_coords[0], i))
        elif y_coords[0] == y_coords[1]:
            for i in range(x_coords[0], x_coords[1]+1):
                line.append((i, y_coords[0]))
        else:
            step_range = int((y_coords[0]-y_coords[1])/(x_coords[0]-x_coords[1]))
            cur_step = 0
            for i in range(x_coords[0], x_coords[1]+1, step_range):
                cur_step+=1
                line.append(
                    (x_coords[0] + cur_step,
                    y_coords[0] + cur_step)
                )
        grid_entries.append(line)
    grid_entries = chain.from_iterable(grid_entries)
    
    for entry in grid_entries:
        x = entry[0]
        y = entry[1]
        grid[x][y]+=1
    
    abc = 0
    for row in grid:
        for cel in row:
            if cel >= 2:
                abc+=1
    
    print(abc)

    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"")
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
    solve_puzzle_1(transfrmd_inp, create_base_grid())
    # solve_puzzle_2(transfrmd_inp)
