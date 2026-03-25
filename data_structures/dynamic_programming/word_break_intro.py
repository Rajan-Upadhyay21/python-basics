# ---------------------------------------------------------
# Program: Word Break
# Description:
# This program checks whether a string can be segmented
# into valid dictionary words using dynamic programming.
# ---------------------------------------------------------

def word_break(text, word_dict):
    dp = [False] * (len(text) + 1)
    dp[0] = True

    for i in range(1, len(text) + 1):
        for j in range(i):
            if dp[j] and text[j:i] in word_dict:
                dp[i] = True
                break

    return dp[len(text)]


text = "leetcode"
word_dict = {"leet", "code"}

print("Text:", text)
print("Dictionary:", word_dict)
print("Can be segmented:", word_break(text, word_dict))
