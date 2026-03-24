# ---------------------------------------------------------
# Program: Merge Two Files
# Description:
# This program reads data from two files and combines both
# into a third file.
# ---------------------------------------------------------

file1 = "file1.txt"
file2 = "file2.txt"
merged_file = "merged_output.txt"

# Creating sample data for file1
with open(file1, "w") as f1:
    f1.write("This is the first file.\n")
    f1.write("It contains some sample text.\n")

# Creating sample data for file2
with open(file2, "w") as f2:
    f2.write("This is the second file.\n")
    f2.write("It also contains sample text.\n")

# Reading both files
with open(file1, "r") as f1:
    content1 = f1.read()

with open(file2, "r") as f2:
    content2 = f2.read()

# Writing merged content
with open(merged_file, "w") as output:
    output.write("Content from File 1:\n")
    output.write(content1)
    output.write("\nContent from File 2:\n")
    output.write(content2)

print("Both files have been merged into", merged_file)
