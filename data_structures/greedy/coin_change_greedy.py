# ---------------------------------------------------------
# Program: Coin Change Greedy
# Description:
# This program finds the minimum number of coins needed
# using a greedy strategy for standard denominations.
# ---------------------------------------------------------

def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


coins = [1, 2, 5, 10, 20, 50, 100]
amount = 93

used_coins = coin_change(coins, amount)

print("Coins used to make amount:")
print(used_coins)
print("Total number of coins:", len(used_coins))
