# ---------------------------------------------------------
# Program: GCD using Recursion
# Description:
# This program finds the Greatest Common Divisor (GCD)
# of two numbers using Euclid's recursive algorithm.
#
# Logic:
# gcd(a, b) = gcd(b, a % b)
# gcd(a, 0) = a
# ---------------------------------------------------------

def gcd(a, b):
    # Base case
    if b == 0:
        return a

    # Recursive case
    return gcd(b, a % b)


# Example numbers
num1 = 48
num2 = 18

# Finding GCD
result = gcd(num1, num2)

# Printing the output
print("GCD of", num1, "and", num2, "is:", result)
