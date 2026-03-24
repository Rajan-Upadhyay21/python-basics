# ---------------------------------------------------------
# Program: Read a File
# Description:
# This program reads the complete content of a text file
# and displays it on the screen.
# ---------------------------------------------------------

file_name = "sample_write.txt"

# Opening file in read mode
with open(file_name, "r") as file:
    content = file.read()

print("File content:\n")
print(content)
