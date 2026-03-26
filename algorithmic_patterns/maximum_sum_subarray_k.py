# ---------------------------------------------------------
# Program: Maximum Sum Subarray of Size K
# Description:
# This program finds the maximum sum of any subarray
# of size k using sliding window.
# ---------------------------------------------------------

def maximum_sum_subarray(numbers, k):
    window_sum = sum(numbers[:k])
    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


numbers = [2, 1, 5, 1, 3, 2]
k = 3

print("Maximum sum:", maximum_sum_subarray(numbers, k))
