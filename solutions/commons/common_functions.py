from typing import Dict


def calc_diff(
    previous_measure: int,
    current_measure: int,
    debug: bool = False,
) -> int:
    diff = current_measure - previous_measure
    if debug:
        print(
            f"Running comparison for: {previous_measure} minus {current_measure}, difference is: {diff}"
        )
    return diff


TOTAL_EQUAL = 0
TOTAL_INCREASE = 0
TOTAL_DECREASE = 0


def manage_differences(diff: int) -> None:
    global TOTAL_EQUAL
    global TOTAL_INCREASE
    global TOTAL_DECREASE
    if diff == 0:
        TOTAL_EQUAL += 1
    elif diff > 0:
        TOTAL_INCREASE += 1
    elif diff < 0:
        TOTAL_DECREASE += 1
    else:
        print("Something is wrong dumdum!")


def get_differences() -> Dict[str, int]:
    global TOTAL_EQUAL
    global TOTAL_INCREASE
    global TOTAL_DECREASE
    return {
        "equals": TOTAL_EQUAL,
        "increase": TOTAL_INCREASE,
        "decrease": TOTAL_DECREASE,
    }
