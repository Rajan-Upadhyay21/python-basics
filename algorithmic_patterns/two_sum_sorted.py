# ---------------------------------------------------------
# Program: Two Sum in Sorted Array
# Description:
# This program finds two numbers in a sorted array
# whose sum equals the target using two pointers.
# ---------------------------------------------------------

def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


numbers = [2, 7, 11, 15]
target = 9

print("Indices:", two_sum_sorted(numbers, target))
