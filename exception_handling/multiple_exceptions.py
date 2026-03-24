# ---------------------------------------------------------
# Program: Handling Multiple Exceptions
# Description:
# This program demonstrates how to handle more than one
# type of exception in a single program.
# ---------------------------------------------------------

try:
    number = int("abc")
    result = 10 / 0
    print(result)

except ValueError:
    print("Error: Invalid conversion to integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as error:
    print("Unexpected error:", error)
