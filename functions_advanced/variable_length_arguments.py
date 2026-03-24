# Defining a function that accepts multiple values
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Calling the function
print("Total =", add_all(10, 20, 30, 40))
