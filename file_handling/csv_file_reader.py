# ---------------------------------------------------------
# Program: Read a CSV File
# Description:
# This program reads data from a CSV file and prints each row.
# ---------------------------------------------------------

import csv

file_name = "students.csv"

try:
    # Create sample CSV file
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course"])
        writer.writerow([1, "Rajan", 23, "Computer Science"])
        writer.writerow([2, "Amit", 22, "Data Science"])
        writer.writerow([3, "Priya", 21, "AI"])

    # Read CSV file
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        print("CSV File Content:\n")
        for row in reader:
            print(row)

except Exception as error:
    print("Unexpected error:", error)
