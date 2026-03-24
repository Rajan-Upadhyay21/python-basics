# ---------------------------------------------------------
# Program: Extract Email Addresses from a File
# Description:
# This program reads a file and extracts all email addresses
# using regular expressions.
# ---------------------------------------------------------

import re

file_name = "emails.txt"

try:
    # Create sample file
    with open(file_name, "w") as file:
        file.write("Contact us at support@example.com\n")
        file.write("You can also email admin@test.org for help.\n")
        file.write("Another email is rajan123@gmail.com\n")

    # Read file content
    with open(file_name, "r") as file:
        content = file.read()

    # Regular expression for emails
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(email_pattern, content)

    print("Extracted Email Addresses:\n")
    for email in emails:
        print(email)

except Exception as error:
    print("Unexpected error:", error)
