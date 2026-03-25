# ---------------------------------------------------------
# Program: Partition Labels
# Description:
# This program partitions a string into as many parts
# as possible so that each letter appears in at most one part.
# ---------------------------------------------------------

def partition_labels(text):
    last_occurrence = {char: index for index, char in enumerate(text)}
    result = []

    start = 0
    end = 0

    for i, char in enumerate(text):
        end = max(end, last_occurrence[char])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


text = "ababcbacadefegdehijhklij"

print("Text:", text)
print("Partition sizes:", partition_labels(text))
