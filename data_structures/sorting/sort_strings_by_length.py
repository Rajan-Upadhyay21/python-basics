# ---------------------------------------------------------
# Program: Sort Strings by Length
# Description:
# This program sorts a list of strings by their length.
# ---------------------------------------------------------

def sort_by_length(words):
    return sorted(words, key=len)


words = ["python", "ai", "machine", "ml", "data", "chatgpt"]

print("Original words:", words)
print("Sorted by length:", sort_by_length(words))
