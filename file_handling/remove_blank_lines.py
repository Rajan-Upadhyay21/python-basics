# ---------------------------------------------------------
# Program: Remove Blank Lines from a File
# Description:
# This program removes all blank lines from an input file
# and saves the cleaned content into another file.
# ---------------------------------------------------------

input_file = "sample_with_blanks.txt"
output_file = "cleaned_file.txt"

try:
    # Create a sample file with blank lines
    with open(input_file, "w") as file:
        file.write("Python is powerful.\n\n")
        file.write("File handling is useful.\n\n")
        file.write("This line comes after a blank line.\n")

    # Read the file and remove blank lines
    with open(input_file, "r") as file:
        lines = file.readlines()

    cleaned_lines = [line for line in lines if line.strip() != ""]

    # Write cleaned content to output file
    with open(output_file, "w") as file:
        file.writelines(cleaned_lines)

    print(f"Blank lines removed successfully.")
    print(f"Cleaned content saved in {output_file}.")

except Exception as error:
    print("Unexpected error:", error)
