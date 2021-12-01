# Calculate the number of increases and decreases.
from puzzle_input import measurement_report, test_report

TOTAL_EQUAL = 0
TOTAL_INCREASE = 0
TOTAL_DECREASE = 0


def calc_diff(
    previous_measure: int,
    current_measure: int,
    total_equal: int = TOTAL_EQUAL,
    total_increases: int = TOTAL_INCREASE,
    total_decreases: int = TOTAL_DECREASE,
    debug: bool = False,
) -> None:
    global TOTAL_EQUAL
    global TOTAL_INCREASE
    global TOTAL_DECREASE
    diff = current_measure - previous_measure
    if debug:
        print(
            f"Running comparison for: {previous_measure} minus {current_measure}, difference is: {diff}"
        )
    if diff == 0:
        TOTAL_EQUAL += 1
    elif diff > 0:
        TOTAL_INCREASE += 1
    elif diff < 0:
        TOTAL_DECREASE += 1
    else:
        print("Something is wrong dumdum!")


previous_window = []
report = measurement_report

for i in range(len(report)):
    if i == 0:
        None  # First entry knows no diff
    else:
        calc_diff(
            current_measure=measurement_report[i],
            previous_measure=measurement_report[i - 1],
        )

print(
    f"Entries: {len(report)}, Number of increases: {TOTAL_INCREASE}, number of decreases: {TOTAL_DECREASE}, number of equals: {TOTAL_EQUAL}"
)
