# ---------------------------------------------------------
# Program: Palindrome Partitioning
# Description:
# This program generates all palindrome partitions of a string
# using backtracking.
# ---------------------------------------------------------

def is_palindrome(text):
    return text == text[::-1]


def partition(text, start, current, result):
    if start == len(text):
        result.append(current[:])
        return

    for end in range(start + 1, len(text) + 1):
        substring = text[start:end]

        if is_palindrome(substring):
            current.append(substring)
            partition(text, end, current, result)
            current.pop()


text = "aab"
result = []

partition(text, 0, [], result)

print("Palindrome partitions:")
for partition_result in result:
    print(partition_result)
