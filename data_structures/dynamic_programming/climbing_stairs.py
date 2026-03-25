# ---------------------------------------------------------
# Program: Climbing Stairs
# Description:
# This program finds the number of distinct ways
# to climb to the top of a staircase.
# ---------------------------------------------------------

def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


steps = 5

print("Number of ways to climb", steps, "steps:", climb_stairs(steps))
