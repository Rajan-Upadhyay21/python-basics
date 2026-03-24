# ---------------------------------------------------------
# Program: Count Word Frequency in a File
# Description:
# This program reads a text file and counts how many times
# each word appears in the file.
# ---------------------------------------------------------

file_name = "word_frequency.txt"

try:
    # Create a sample file
    with open(file_name, "w") as file:
        file.write("python is powerful and python is easy to learn\n")
        file.write("machine learning with python is interesting\n")

    # Read file content
    with open(file_name, "r") as file:
        content = file.read().lower()

    # Split into words
    words = content.split()

    # Count frequency
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("Word Frequency Analysis:\n")
    for word, count in frequency.items():
        print(f"{word}: {count}")

except Exception as error:
    print("Unexpected error:", error)
