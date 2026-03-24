# ---------------------------------------------------------
# Program: Log File Analyzer
# Description:
# This program analyzes a log file and counts the number of
# INFO, WARNING, and ERROR messages.
# ---------------------------------------------------------

file_name = "application.log"

try:
    # Create sample log file
    with open(file_name, "w") as file:
        file.write("INFO: Application started successfully\n")
        file.write("WARNING: Disk space is running low\n")
        file.write("ERROR: Failed to connect to database\n")
        file.write("INFO: User logged in\n")
        file.write("ERROR: Invalid user input\n")
        file.write("WARNING: High memory usage detected\n")

    # Read log file
    with open(file_name, "r") as file:
        lines = file.readlines()

    info_count = 0
    warning_count = 0
    error_count = 0

    for line in lines:
        if line.startswith("INFO"):
            info_count += 1
        elif line.startswith("WARNING"):
            warning_count += 1
        elif line.startswith("ERROR"):
            error_count += 1

    print("Log File Analysis:\n")
    print("INFO messages   :", info_count)
    print("WARNING messages:", warning_count)
    print("ERROR messages  :", error_count)

except Exception as error:
    print("Unexpected error:", error)
