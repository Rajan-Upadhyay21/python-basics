# ---------------------------------------------------------
# Program: Read and Write JSON File
# Description:
# This program writes Python dictionary data into a JSON file
# and then reads it back.
# ---------------------------------------------------------

import json

file_name = "student_data.json"

student_data = {
    "name": "Rajan",
    "age": 23,
    "course": "Computer Science",
    "skills": ["Python", "Machine Learning", "Data Analysis"]
}

try:
    # Write dictionary to JSON file
    with open(file_name, "w") as file:
        json.dump(student_data, file, indent=4)

    print("JSON data written successfully.\n")

    # Read JSON file
    with open(file_name, "r") as file:
        loaded_data = json.load(file)

    print("Data read from JSON file:\n")
    print(loaded_data)

except Exception as error:
    print("Unexpected error:", error)
