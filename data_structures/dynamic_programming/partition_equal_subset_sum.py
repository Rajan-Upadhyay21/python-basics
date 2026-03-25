# ---------------------------------------------------------
# Program: Partition Equal Subset Sum
# Description:
# This program checks whether the array can be partitioned
# into two subsets with equal sum.
# ---------------------------------------------------------

def can_partition(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for current_sum in range(target, num - 1, -1):
            dp[current_sum] = dp[current_sum] or dp[current_sum - num]

    return dp[target]


numbers = [1, 5, 11, 5]

print("Numbers:", numbers)
print("Can partition into equal subsets:", can_partition(numbers))
