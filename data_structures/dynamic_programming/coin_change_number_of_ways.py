# ---------------------------------------------------------
# Program: Coin Change Number of Ways
# Description:
# This program counts the number of ways to make an amount
# using given coin denominations.
# ---------------------------------------------------------

def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]

    return dp[amount]


coins = [1, 2, 5]
amount = 5

print("Coins:", coins)
print("Amount:", amount)
print("Number of ways:", count_ways(coins, amount))
