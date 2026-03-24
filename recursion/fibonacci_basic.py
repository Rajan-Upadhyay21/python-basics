# ---------------------------------------------------------
# Program: Fibonacci Series using Recursion
# Description:
# This program prints the Fibonacci sequence using recursion.
# In Fibonacci:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)
# ---------------------------------------------------------

def fibonacci(n):
    # Base case 1
    if n == 0:
        return 0

    # Base case 2
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Number of terms to print
terms = 10

print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
