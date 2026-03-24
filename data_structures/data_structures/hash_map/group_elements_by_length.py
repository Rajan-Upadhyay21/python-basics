# ---------------------------------------------------------
# Program: Group Elements by Length
# Description:
# This program groups strings based on their length
# using a hash map.
# ---------------------------------------------------------

words = ["ai", "python", "ml", "data", "deep", "code", "chatgpt"]
grouped = {}

for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(word)

print("Words grouped by length:")
for length, word_list in grouped.items():
    print(length, ":", word_list)
