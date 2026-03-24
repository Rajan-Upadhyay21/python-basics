# ---------------------------------------------------------
# Program: Search for a Word in a File
# Description:
# This program searches for a specific word in a text file
# and counts how many times it appears.
# ---------------------------------------------------------

file_name = "sample_write.txt"
search_word = "file"

with open(file_name, "r") as file:
    content = file.read().lower()

# Counting occurrences of the search word
count = content.count(search_word.lower())

print("The word", "'" + search_word + "'", "appears", count, "times in", file_name)
