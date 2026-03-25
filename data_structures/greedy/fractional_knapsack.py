# ---------------------------------------------------------
# Program: Fractional Knapsack
# Description:
# This program solves the fractional knapsack problem
# using a greedy approach.
# ---------------------------------------------------------

def fractional_knapsack(values, weights, capacity):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))

    items.sort(reverse=True)

    total_value = 0

    for ratio, value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    return total_value


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Maximum value in knapsack:", fractional_knapsack(values, weights, capacity))
