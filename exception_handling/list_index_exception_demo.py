# ---------------------------------------------------------
# Program: List Index Exception Demo
# Description:
# This program handles invalid list index access.
# ---------------------------------------------------------

numbers = [1, 2, 3, 4]

try:
    print(numbers[10])

except IndexError:
    print("Error: Index out of range.")
