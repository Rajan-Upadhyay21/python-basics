# ---------------------------------------------------------
# Program: Longest Common Subsequence
# Description:
# This program finds the length of the longest common
# subsequence between two strings using dynamic programming.
# ---------------------------------------------------------

def lcs(text1, text2):
    rows = len(text1) + 1
    cols = len(text2) + 1

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(text1)][len(text2)]


text1 = "abcde"
text2 = "ace"

print("String 1:", text1)
print("String 2:", text2)
print("Length of LCS:", lcs(text1, text2))
