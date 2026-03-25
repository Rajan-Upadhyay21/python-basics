# ---------------------------------------------------------
# Program: 0/1 Knapsack
# Description:
# This program solves the 0/1 knapsack problem
# using dynamic programming.
# ---------------------------------------------------------

def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for current_capacity in range(1, capacity + 1):
            if weights[i - 1] <= current_capacity:
                dp[i][current_capacity] = max(
                    values[i - 1] + dp[i - 1][current_capacity - weights[i - 1]],
                    dp[i - 1][current_capacity]
                )
            else:
                dp[i][current_capacity] = dp[i - 1][current_capacity]

    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)
print("Maximum value in knapsack:", knapsack(weights, values, capacity))
