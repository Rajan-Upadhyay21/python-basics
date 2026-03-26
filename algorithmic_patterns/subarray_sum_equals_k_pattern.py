# ---------------------------------------------------------
# Program: Subarray Sum Equals K
# Description:
# This program counts the number of subarrays whose sum
# equals a target using prefix sum and hash map.
# ---------------------------------------------------------

def subarray_sum_equals_k(numbers, k):
    prefix_sum_count = {0: 1}
    current_sum = 0
    count = 0

    for number in numbers:
        current_sum += number

        if current_sum - k in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]

        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count


numbers = [1, 2, 3, -2, 2, 1, 1]
target = 4

print("Array:", numbers)
print("Target:", target)
print("Subarrays with target sum:", subarray_sum_equals_k(numbers, target))
