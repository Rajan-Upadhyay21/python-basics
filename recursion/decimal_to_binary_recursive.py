# ---------------------------------------------------------
# Program: Decimal to Binary using Recursion
# Description:
# This program converts a decimal number into binary using
# recursion.
#
# Logic:
# binary(n) = binary(n // 2) + remainder
# ---------------------------------------------------------

def decimal_to_binary(n):
    # Base case
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    # Recursive case
    return decimal_to_binary(n // 2) + str(n % 2)


# Input number
number = 25

# Function call
binary_value = decimal_to_binary(number)

# Output
print("Decimal number:", number)
print("Binary equivalent:", binary_value)
