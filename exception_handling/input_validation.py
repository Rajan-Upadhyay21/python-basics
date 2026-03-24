# ---------------------------------------------------------
# Program: Input Validation with Exception Handling
# Description:
# This program validates user input and handles invalid
# numeric conversion safely.
# ---------------------------------------------------------

try:
    user_input = "abc"   # Replace with input("Enter a number: ")
    number = int(user_input)

    print("You entered:", number)

except ValueError:
    print("Error: Please enter a valid integer.")
