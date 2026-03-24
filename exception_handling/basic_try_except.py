# ---------------------------------------------------------
# Program: Basic Try-Except Example
# Description:
# This program handles division by zero using try-except.
# ---------------------------------------------------------

try:
    numerator = 10
    denominator = 0

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
