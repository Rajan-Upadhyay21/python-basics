# Finding factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Calling the function
print("Factorial =", factorial(5))
