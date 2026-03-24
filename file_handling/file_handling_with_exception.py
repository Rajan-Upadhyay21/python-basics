# ---------------------------------------------------------
# Program: File Handling with Exception Handling
# Description:
# This program safely opens and reads a file. If the file
# does not exist, it handles the error gracefully.
# ---------------------------------------------------------

file_name = "non_existing_file.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file", file_name, "was not found.")

except Exception as error:
    print("An unexpected error occurred:", error)

finally:
    print("File handling operation completed.")
