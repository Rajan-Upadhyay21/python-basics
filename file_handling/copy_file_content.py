# ---------------------------------------------------------
# Program: Copy File Content
# Description:
# This program copies the content of one file into another file.
# ---------------------------------------------------------

source_file = "sample_write.txt"
destination_file = "copied_file.txt"

# Reading source file content
with open(source_file, "r") as source:
    data = source.read()

# Writing data into destination file
with open(destination_file, "w") as destination:
    destination.write(data)

print("Content copied successfully from", source_file, "to", destination_file)
