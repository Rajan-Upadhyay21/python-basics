# ---------------------------------------------------------
# Program: Minimum Size Subarray Sum
# Description:
# This program finds the minimum length of a contiguous
# subarray whose sum is at least target.
# ---------------------------------------------------------

def min_subarray_len(target, numbers):
    left = 0
    current_sum = 0
    result = float("inf")

    for right in range(len(numbers)):
        current_sum += numbers[right]

        while current_sum >= target:
            result = min(result, right - left + 1)
            current_sum -= numbers[left]
            left += 1

    return 0 if result == float("inf") else result


numbers = [2, 3, 1, 2, 4, 3]
target = 7

print("Minimum subarray length:", min_subarray_len(target, numbers))
