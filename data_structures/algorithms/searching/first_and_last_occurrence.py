# ---------------------------------------------------------
# Program: First and Last Occurrence
# Description:
# This program finds the first and last occurrence of a
# target element in a sorted array.
# ---------------------------------------------------------

def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


numbers = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
target = 5

first = find_first_occurrence(numbers, target)
last = find_last_occurrence(numbers, target)

print("Array:", numbers)
print("Target:", target)
print("First occurrence:", first)
print("Last occurrence:", last)
