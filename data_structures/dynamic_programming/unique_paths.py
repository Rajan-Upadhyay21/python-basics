# ---------------------------------------------------------
# Program: Unique Paths
# Description:
# This program finds the number of unique paths
# in a grid using dynamic programming.
# ---------------------------------------------------------

def unique_paths(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


rows = 3
cols = 7

print("Grid size:", rows, "x", cols)
print("Unique paths:", unique_paths(rows, cols))
