# ---------------------------------------------------------
# Program: Coin Change Minimum Coins
# Description:
# This program finds the minimum number of coins needed
# to make a given amount using dynamic programming.
# ---------------------------------------------------------

def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if value - coin >= 0:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 11

print("Coins:", coins)
print("Amount:", amount)
print("Minimum coins needed:", coin_change(coins, amount))
