# ---------------------------------------------------------
# Program: Append Data to a File
# Description:
# This program adds new content at the end of an existing file
# without deleting the previous data.
# ---------------------------------------------------------

file_name = "sample_write.txt"

# Opening file in append mode
with open(file_name, "a") as file:
    file.write("This line was added later using append mode.\n")
    file.write("Appending is useful when we want to preserve old data.\n")

print("New content has been appended to", file_name)
