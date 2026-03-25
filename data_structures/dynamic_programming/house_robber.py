# ---------------------------------------------------------
# Program: House Robber
# Description:
# This program finds the maximum amount of money
# that can be robbed without robbing adjacent houses.
# ---------------------------------------------------------

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


houses = [2, 7, 9, 3, 1]

print("House values:", houses)
print("Maximum money that can be robbed:", rob(houses))
