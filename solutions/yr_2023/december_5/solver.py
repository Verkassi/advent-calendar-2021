from copy import deepcopy
from pathlib import Path
from tqdm import tqdm

def read_input(is_test: bool = False):
    if is_test:
        input_file = Path("inputs/test.txt")
    else:
        input_file = Path("inputs/actual.txt")

    with open(input_file) as file:
        content = file.read().split('\n\n')
    return content

def convert_input(is_test: bool = False):

    def _calc_ranges(conversion_rows):

        return_values = list()

        for conversion_row in conversion_rows:
            conversion = dict()

            conversion_row = conversion_row.split()
            conversion['source_start'] = int(conversion_row[1])
            conversion['source_end'] = int(conversion_row[1]) + ( int(conversion_row[2]) - 1 )
            conversion['addition'] = int(conversion_row[0]) - int(conversion_row[1])

            return_values.append(conversion)

        return return_values

    puzzle = read_input(is_test=is_test)

    almenac_basemap = dict()

    # Seeds
    almenac_basemap["seeds"] = puzzle[0].replace('seeds: ', '').split()

    # Seed 2 Soil
    almenac_basemap["seed2soil"] = _calc_ranges(puzzle[1].replace('seed-to-soil map:\n', '').split('\n'))

    # Soil 2 Fertalizer
    almenac_basemap["soil2fertalizer"] = _calc_ranges(puzzle[2].replace('soil-to-fertilizer map:\n', '').split('\n'))

    # Fertalizer 2 Water
    almenac_basemap["fertalizer2water"] = _calc_ranges(puzzle[3].replace('fertilizer-to-water map:\n', '').split('\n'))

    # Water 2 Light
    almenac_basemap["water2light"] = _calc_ranges(puzzle[4].replace('water-to-light map:\n', '').split('\n'))

    # Light 2 Temperature
    almenac_basemap["light2temperature"] = _calc_ranges(puzzle[5].replace('light-to-temperature map:\n', '').split('\n'))

    # Temperature 2 Humidity
    almenac_basemap["temperature2humidity"] = _calc_ranges(puzzle[6].replace('temperature-to-humidity map:\n', '').split('\n'))

    # Humidity 2 Location
    almenac_basemap["humidity2location"] = _calc_ranges(puzzle[7].replace('humidity-to-location map:\n', '').split('\n'))

    return almenac_basemap

def solve_puzzle_1(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    def _convert(position: int, lookup_table):
        new_pos = [ position + conversion_range['addition'] for conversion_range in lookup_table if conversion_range['source_end'] >= position >= conversion_range['source_start'] ]
        if new_pos:
            return new_pos[0]
        else:
            return position

    locations = set()

    for seed in puzzle['seeds']:
        soil = _convert(position=int(seed), lookup_table=puzzle["seed2soil"])
        fertilizer = _convert(position=soil, lookup_table=puzzle["soil2fertalizer"])
        water = _convert(position=fertilizer, lookup_table=puzzle["fertalizer2water"])
        light = _convert(position=water, lookup_table=puzzle["water2light"])
        temperature = _convert(position=light, lookup_table=puzzle["light2temperature"])
        humidity = _convert(position=temperature, lookup_table=puzzle["temperature2humidity"])
        location = _convert(position=humidity, lookup_table=puzzle["humidity2location"])

        locations.add(location)


    print("---------------- PUZZLE ONE SOLUTION ----------------")
    print(f"{min(locations)}")
    print("-----------------------------------------------------")


def solve_puzzle_2(puzzle_in: list) -> None:
    puzzle = deepcopy(puzzle_in)

    def _convert_seeds(seeds: list):
        seed_ranges = list()

        for i in range(len(seeds)):
            if (i % 2) == 0:
                range_first = int(seeds[i])
                range_last = int(seeds[i]) + int(seeds[i+1])
                calculated_seed_range = range(range_first, range_last)
                seed_ranges.append(calculated_seed_range)

        return seed_ranges

    def _convert(position: int, lookup_table):
        for conversion_range in lookup_table:
            if conversion_range['source_end'] >= position >= conversion_range['source_start']:
                return (position + conversion_range['addition'])
        return position

    seed_ranges = _convert_seeds(
        seeds=puzzle['seeds']
    )

    locations = set()

    print(f"Going to calculate these ranges: {seed_ranges}")
    for seed_range in tqdm(seed_ranges):
        print(f"Starting with range: {seed_range}")
        current_locations = set()
        for seed in tqdm(seed_range):
            soil = _convert(position=int(seed), lookup_table=puzzle["seed2soil"])
            fertilizer = _convert(position=soil, lookup_table=puzzle["soil2fertalizer"])
            water = _convert(position=fertilizer, lookup_table=puzzle["fertalizer2water"])
            light = _convert(position=water, lookup_table=puzzle["water2light"])
            temperature = _convert(position=light, lookup_table=puzzle["light2temperature"])
            humidity = _convert(position=temperature, lookup_table=puzzle["temperature2humidity"])
            location = _convert(position=humidity, lookup_table=puzzle["humidity2location"])

            current_locations.add(location)
        locations.add(min(current_locations))

    print("---------------- PUZZLE TWO SOLUTION ----------------")
    print(f"{min(locations)}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    transfrmd_inp_p1 = convert_input(is_test=False)
    solve_puzzle_1(transfrmd_inp_p1)
    transfrmd_inp_p2 = convert_input(is_test=False)
    solve_puzzle_2(transfrmd_inp_p2)
