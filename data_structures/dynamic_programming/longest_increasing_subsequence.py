# ---------------------------------------------------------
# Program: Longest Increasing Subsequence
# Description:
# This program finds the length of the longest increasing
# subsequence in an array using dynamic programming.
# ---------------------------------------------------------

def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


numbers = [10, 9, 2, 5, 3, 7, 101, 18]

print("Array:", numbers)
print("Length of LIS:", length_of_lis(numbers))
