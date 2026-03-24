# ---------------------------------------------------------
# Program: Count Occurrences Using Binary Search
# Description:
# This program counts the occurrences of a target value
# in a sorted array using binary search.
# ---------------------------------------------------------

def first_occurrence(arr, target):
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


def last_occurrence(arr, target):
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


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1


numbers = [2, 4, 4, 4, 6, 6, 8, 10]
target = 4

print("Array:", numbers)
print("Target:", target)
print("Occurrences:", count_occurrences(numbers, target))
