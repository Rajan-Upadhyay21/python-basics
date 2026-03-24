# ---------------------------------------------------------
# Program: Power of a Number using Recursion
# Description:
# This program calculates a number raised to a power using
# recursion.
#
# Example:
# 2^5 = 2 * 2 * 2 * 2 * 2 = 32
# ---------------------------------------------------------

def power(base, exponent):
    # Base case
    if exponent == 0:
        return 1

    # Recursive case
    return base * power(base, exponent - 1)


# Given values
base_number = 2
exponent_value = 5

# Calling the recursive function
result = power(base_number, exponent_value)

# Printing the result
print(base_number, "raised to the power", exponent_value, "is:", result)
