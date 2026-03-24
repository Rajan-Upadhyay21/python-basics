# ---------------------------------------------------------
# Program: Resource Cleanup Manager
# Description:
# This program demonstrates the use of finally to ensure
# that cleanup code always runs, even if an exception occurs.
# ---------------------------------------------------------

resource_open = False

try:
    print("Opening resource...")
    resource_open = True

    print("Performing operation on resource...")
    result = 10 / 0
    print("Result:", result)

except ZeroDivisionError as error:
    print("Error during resource operation:", error)

finally:
    if resource_open:
        print("Closing resource safely...")
        resource_open = False

    print("Cleanup process completed.")
