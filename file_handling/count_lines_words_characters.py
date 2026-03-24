# ---------------------------------------------------------
# Program: Count Lines, Words, and Characters in a File
# Description:
# This program reads a text file and counts:
# 1. Total number of lines
# 2. Total number of words
# 3. Total number of characters
# ---------------------------------------------------------

file_name = "sample_write.txt"

with open(file_name, "r") as file:
    content = file.read()

# Counting characters
character_count = len(content)

# Counting words
word_count = len(content.split())

# Counting lines
line_count = len(content.splitlines())

print("Analysis of file:", file_name)
print("Total lines:", line_count)
print("Total words:", word_count)
print("Total characters:", character_count)
