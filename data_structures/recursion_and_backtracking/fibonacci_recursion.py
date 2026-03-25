# ---------------------------------------------------------
# Program: Fibonacci Using Recursion
# Description:
# This program prints Fibonacci numbers using recursion.
# ---------------------------------------------------------

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


terms = 8

print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
