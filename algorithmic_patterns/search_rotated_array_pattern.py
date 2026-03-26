# ---------------------------------------------------------
# Program: Search in Rotated Sorted Array
# Description:
# This program searches for a target value in a rotated
# sorted array using the binary search pattern.
# ---------------------------------------------------------

def search_rotated_array(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        if numbers[left] <= numbers[mid]:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


numbers = [15, 18, 2, 3, 6, 12]
target = 3

print("Rotated sorted array:", numbers)
print("Target:", target)
print("Target index:", search_rotated_array(numbers, target))
