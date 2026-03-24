# ---------------------------------------------------------
# Program: Replace a Word in a File
# Description:
# This program reads the content of a file, replaces all
# occurrences of one word with another, and writes the
# updated content back to a new file.
# ---------------------------------------------------------

input_file = "sample_write.txt"
output_file = "updated_file.txt"

old_word = "file"
new_word = "document"

try:
    # Read original file
    with open(input_file, "r") as file:
        content = file.read()

    # Replace target word
    updated_content = content.replace(old_word, new_word)

    # Write updated content to new file
    with open(output_file, "w") as file:
        file.write(updated_content)

    print(f"All occurrences of '{old_word}' were replaced with '{new_word}'.")
    print(f"Updated content has been saved to {output_file}.")

except FileNotFoundError:
    print(f"Error: {input_file} does not exist.")

except Exception as error:
    print("Unexpected error:", error)
