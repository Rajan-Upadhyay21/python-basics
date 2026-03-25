# ---------------------------------------------------------
# Program: Edit Distance
# Description:
# This program finds the minimum number of operations
# required to convert one string into another.
# ---------------------------------------------------------

def edit_distance(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = i

    for j in range(cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

    return dp[len(word1)][len(word2)]


word1 = "horse"
word2 = "ros"

print("Word 1:", word1)
print("Word 2:", word2)
print("Edit distance:", edit_distance(word1, word2))
