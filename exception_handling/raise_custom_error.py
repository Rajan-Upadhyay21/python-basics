# ---------------------------------------------------------
# Program: Raising Exceptions Manually
# Description:
# This program raises a custom exception manually when
# an invalid value is detected.
# ---------------------------------------------------------

age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age:", age)

except ValueError as error:
    print("Error:", error)
