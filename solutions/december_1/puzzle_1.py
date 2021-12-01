import sys

sys.path.append("../../solutions")

from commons import common_functions as cf
from input_data.advent_input import measurement_report
from input_data.test_input import test_report

report = measurement_report

for i in range(len(report)):
    if i == 0:
        None  # First entry knows no diff
    else:
        cf.manage_differences(
            cf.calc_diff(
                current_measure=report[i],
                previous_measure=report[i - 1],
            )
        )

differences = cf.get_differences()

print(differences)
