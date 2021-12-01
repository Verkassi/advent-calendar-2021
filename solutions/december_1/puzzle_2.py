import sys
from typing import List

sys.path.append("../../solutions")

from commons import common_functions as cf
from input_data.advent_input import measurement_report
from input_data.test_input import test_report

previous_window: List[int] = []
report = measurement_report

for i in range(len(report)):
    if i >= (len(report) - 2):
        print("Last windows have been calculated.")
        break
    else:
        current_window = [
            report[i],
            report[i + 1],
            report[i + 2],
        ]
        if i == 0:
            None  # First entry knows no diff
        else:
            cf.manage_differences(
                cf.calc_diff(
                    current_measure=sum(current_window),
                    previous_measure=sum(previous_window),
                )
            )
        previous_window = current_window  # Save for next iteration

differences = cf.get_differences()

print(differences)
