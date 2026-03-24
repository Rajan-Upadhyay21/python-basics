# ---------------------------------------------------------
# Program: Linear Search
# Description:
# This program searches for a target element by checking
# each element one by one.
# ---------------------------------------------------------

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


numbers = [12, 45, 7, 23, 56, 91, 18]
target = 23

result = linear_search(numbers, target)

print("Array:", numbers)
print("Target:", target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
