# ---------------------------------------------------------
# Program: Write to a File
# Description:
# This program creates a text file and writes content into it.
# If the file already exists, its old content will be replaced.
# ---------------------------------------------------------

file_name = "sample_write.txt"

# Opening file in write mode
with open(file_name, "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This file is created using Python file handling.\n")
    file.write("Writing to files is very useful for storing data.\n")

print("Data has been written successfully to", file_name)
