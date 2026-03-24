# ---------------------------------------------------------
# Program: Retry Until Valid Input
# Description:
# This program keeps asking until a valid integer is entered.
# ---------------------------------------------------------

while True:
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print("Valid input received:", number)
        break

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
