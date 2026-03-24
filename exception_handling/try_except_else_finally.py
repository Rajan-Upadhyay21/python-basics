# ---------------------------------------------------------
# Program: Try-Except-Else-Finally
# Description:
# This program shows how else runs when no exception occurs
# and finally always runs.
# ---------------------------------------------------------

try:
    number = int("25")
    result = 100 / number

except ValueError:
    print("Error: Invalid integer value.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Division result:", result)

finally:
    print("Program execution completed.")
