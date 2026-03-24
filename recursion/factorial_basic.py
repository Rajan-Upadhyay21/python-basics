# ---------------------------------------------------------
# Program: Factorial using Recursion
# Description:
# This program calculates the factorial of a number using
# recursion. Factorial of n is:
# n! = n * (n-1) * (n-2) * ... * 1
#
# Example:
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# ---------------------------------------------------------

def factorial(n):
    # Base case:
    # If n is 0 or 1, factorial is 1
    if n == 0 or n == 1:
        return 1

    # Recursive case:
    # n! = n * (n-1)!
    return n * factorial(n - 1)


# Main part of the program
number = 5

# Calling the recursive function
result = factorial(number)

# Printing the result
print("Factorial of", number, "is", result)
