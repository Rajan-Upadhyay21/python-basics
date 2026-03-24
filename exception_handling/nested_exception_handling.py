# ---------------------------------------------------------
# Program: Nested Exception Handling
# Description:
# This program demonstrates nested try-except blocks.
# ---------------------------------------------------------

try:
    numbers = [10, 20, 30]

    try:
        index = 5
        print("Value at index:", numbers[index])

    except IndexError:
        print("Inner Error: List index out of range.")

    value = int("100")
    print("Converted value:", value)

except ValueError:
    print("Outer Error: Invalid integer conversion.")

except Exception as error:
    print("Outer Unexpected Error:", error)
