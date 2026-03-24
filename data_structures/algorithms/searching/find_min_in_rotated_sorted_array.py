# ---------------------------------------------------------
# Program: Find Minimum in Rotated Sorted Array
# Description:
# This program finds the minimum element in a rotated
# sorted array using binary search.
# ---------------------------------------------------------

def find_min(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]


numbers = [4, 5, 6, 7, 0, 1, 2]

print("Rotated sorted array:", numbers)
print("Minimum element:", find_min(numbers))
