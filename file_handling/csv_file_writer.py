# ---------------------------------------------------------
# Program: Write Data to a CSV File
# Description:
# This program writes multiple rows of structured data into
# a CSV file using Python's csv module.
# ---------------------------------------------------------

import csv

file_name = "employee_data.csv"

employee_records = [
    ["Employee ID", "Name", "Department", "Salary"],
    [101, "Rajan", "AI Engineer", 85000],
    [102, "Neha", "ML Engineer", 90000],
    [103, "Arjun", "Data Analyst", 70000]
]

try:
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(employee_records)

    print(f"CSV file '{file_name}' created successfully.")
    print("Employee records have been written.")

except Exception as error:
    print("Unexpected error:", error)
