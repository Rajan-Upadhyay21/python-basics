# ---------------------------------------------------------
# Program: Sum of First N Natural Numbers using Recursion
# Description:
# This program finds the sum of the first n natural numbers
# using a recursive function.
#
# Formula idea:
# sum(n) = n + sum(n-1)
# ---------------------------------------------------------

def sum_of_n(n):
    # Base case
    if n == 1:
        return 1

    # Recursive case
    return n + sum_of_n(n - 1)


# Input value
number = 10

# Function call
result = sum_of_n(number)

# Output
print("Sum of first", number, "natural numbers is:", result)
