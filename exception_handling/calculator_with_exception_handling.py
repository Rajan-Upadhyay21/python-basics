# ---------------------------------------------------------
# Program: Calculator with Exception Handling
# Description:
# This program performs division with safe exception handling.
# ---------------------------------------------------------

try:
    num1 = 50
    num2 = 0

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except TypeError:
    print("Error: Invalid data type used in calculation.")

except Exception as error:
    print("Unexpected error:", error)
