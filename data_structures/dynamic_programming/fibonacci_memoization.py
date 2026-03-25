# ---------------------------------------------------------
# Program: Fibonacci with Memoization
# Description:
# This program calculates Fibonacci numbers using
# dynamic programming with memoization.
# ---------------------------------------------------------

def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


number = 10

print("Fibonacci of", number, "is:", fibonacci(number))
