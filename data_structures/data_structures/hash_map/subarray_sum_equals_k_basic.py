# ---------------------------------------------------------
# Program: Subarray Sum Equals K
# Description:
# This program counts the number of continuous subarrays
# whose sum equals a given target.
# ---------------------------------------------------------

def subarray_sum(nums, k):
    prefix_sum_count = {0: 1}
    current_sum = 0
    total_subarrays = 0

    for num in nums:
        current_sum += num

        if current_sum - k in prefix_sum_count:
            total_subarrays += prefix_sum_count[current_sum - k]

        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return total_subarrays


numbers = [1, 2, 3, -2, 2, 1, 1]
target = 4

print("Numbers:", numbers)
print("Target sum:", target)
print("Number of subarrays:", subarray_sum(numbers, target))
