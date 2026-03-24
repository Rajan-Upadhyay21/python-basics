# ---------------------------------------------------------
# Program: Recursive Binary Search
# Description:
# This program searches for a target element in a sorted list
# using recursion. Binary search works by repeatedly dividing
# the search interval into halves.
# ---------------------------------------------------------

def binary_search(arr, left, right, target):
    # Base case: target not found
    if left > right:
        return -1

    # Find the middle index
    mid = (left + right) // 2

    # If target is found at mid
    if arr[mid] == target:
        return mid

    # If target is smaller, search left half
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)

    # If target is larger, search right half
    else:
        return binary_search(arr, mid + 1, right, target)


# Sorted list
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target_value = 38

print("Sorted list:")
print(numbers)
print("Target value:", target_value)

result = binary_search(numbers, 0, len(numbers) - 1, target_value)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the list")
