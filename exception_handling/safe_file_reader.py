# ---------------------------------------------------------
# Program: Safe File Reader
# Description:
# This program safely opens and reads a file while handling
# file-related exceptions.
# ---------------------------------------------------------

file_name = "missing_file.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")

except PermissionError:
    print("Error: Permission denied while accessing the file.")

except Exception as error:
    print("Unexpected error:", error)

finally:
    print("File reading attempt finished.")
