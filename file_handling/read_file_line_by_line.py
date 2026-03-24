# ---------------------------------------------------------
# Program: Read File Line by Line
# Description:
# This program reads a file one line at a time and prints
# line numbers along with each line.
# ---------------------------------------------------------

file_name = "sample_write.txt"

with open(file_name, "r") as file:
    line_number = 1
    for line in file:
        print("Line", line_number, ":", line.strip())
        line_number += 1
