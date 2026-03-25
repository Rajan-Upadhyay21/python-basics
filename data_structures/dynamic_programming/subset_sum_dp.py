# ---------------------------------------------------------
# Program: Subset Sum using DP
# Description:
# This program checks whether a subset exists
# with a given target sum using dynamic programming.
# ---------------------------------------------------------

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for current_sum in range(1, target + 1):
            if nums[i - 1] <= current_sum:
                dp[i][current_sum] = (
                    dp[i - 1][current_sum] or
                    dp[i - 1][current_sum - nums[i - 1]]
                )
            else:
                dp[i][current_sum] = dp[i - 1][current_sum]

    return dp[n][target]


numbers = [3, 34, 4, 12, 5, 2]
target = 9

print("Numbers:", numbers)
print("Target:", target)
print("Subset with target sum exists:", subset_sum(numbers, target))
