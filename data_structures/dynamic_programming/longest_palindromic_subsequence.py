# ---------------------------------------------------------
# Program: Longest Palindromic Subsequence
# Description:
# This program finds the length of the longest palindromic
# subsequence using dynamic programming.
# ---------------------------------------------------------

def longest_palindromic_subsequence(text):
    n = len(text)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if text[i] == text[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


text = "bbbab"

print("Text:", text)
print("Length of longest palindromic subsequence:",
      longest_palindromic_subsequence(text))
