"""
Try to spot the bugs!

Author: Omer Rosenbaum
"""


def calculate_bmi(weight, height):
    """calculates a person's BMI given the persons weight and height"""
    return weight / (height ** 2)


if __name__ == '__main__':
    patients = [(75, 1.81), (82, 1.76), (95, 1.72)]

    for patient in patients:
        weight, height = patient   # weight, height = patients[0] changed to: weight, height = patient
        bmi = calculate_bmi(height=height, weight=weight)   # bmi = calculate_bmi(height, weight) changed to: bmi = calculate_bmi(height=height, weight=weight)
        print("Patient's BMI is: %f" % bmi)
