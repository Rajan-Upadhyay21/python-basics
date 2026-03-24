# ---------------------------------------------------------
# Program: Binary Search
# Description:
# This program searches for a target element in a sorted
# array using the binary search technique.
# ---------------------------------------------------------

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [5, 10, 15, 20, 25, 30, 35, 40]
target = 25

result = binary_search(numbers, target)

print("Sorted array:", numbers)
print("Target:", target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
