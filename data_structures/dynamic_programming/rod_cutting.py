# ---------------------------------------------------------
# Program: Rod Cutting
# Description:
# This program finds the maximum obtainable value
# by cutting up a rod using dynamic programming.
# ---------------------------------------------------------

def rod_cutting(prices, rod_length):
    dp = [0] * (rod_length + 1)

    for length in range(1, rod_length + 1):
        for cut in range(1, length + 1):
            dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])

    return dp[rod_length]


prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8

print("Prices:", prices)
print("Rod length:", rod_length)
print("Maximum obtainable value:", rod_cutting(prices, rod_length))
