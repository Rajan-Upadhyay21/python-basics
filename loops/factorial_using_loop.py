# Finding factorial of a number using loop
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, "is", factorial)
