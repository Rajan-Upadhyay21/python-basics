# ---------------------------------------------------------
# Program: Exception Logging System
# Description:
# This program demonstrates how exceptions can be caught
# and written into a log file for debugging purposes.
# ---------------------------------------------------------

from datetime import datetime

log_file = "error_log.txt"

def divide_numbers(a, b):
    return a / b


try:
    num1 = 25
    num2 = 0

    print("Performing division...")
    result = divide_numbers(num1, num2)
    print("Result:", result)

except Exception as error:
    error_message = f"{datetime.now()} - Error occurred: {str(error)}\n"

    with open(log_file, "a") as file:
        file.write(error_message)

    print("An error occurred and has been logged to", log_file)

finally:
    print("Execution completed.")
