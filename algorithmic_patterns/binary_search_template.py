# ---------------------------------------------------------
# Program: Binary Search Template
# Description:
# This program demonstrates the standard binary search
# pattern on a sorted array.
# ---------------------------------------------------------

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target = 23

print("Sorted array:", numbers)
print("Target:", target)
print("Target index:", binary_search(numbers, target))
