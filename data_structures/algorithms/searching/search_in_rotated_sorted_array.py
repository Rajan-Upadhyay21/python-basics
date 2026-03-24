# ---------------------------------------------------------
# Program: Search in Rotated Sorted Array
# Description:
# This program searches for a target element in a rotated
# sorted array using modified binary search.
# ---------------------------------------------------------

def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


numbers = [13, 18, 25, 2, 8, 10]
target = 8

result = search_rotated(numbers, target)

print("Rotated sorted array:", numbers)
print("Target:", target)
print("Result index:", result)
