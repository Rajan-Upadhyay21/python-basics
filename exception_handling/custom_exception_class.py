# ---------------------------------------------------------
# Program: Custom Exception Class
# Description:
# This program defines and uses a custom exception class.
# ---------------------------------------------------------

class InvalidMarksError(Exception):
    """Custom exception for invalid marks input."""
    pass


def check_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    return "Valid marks entered."


try:
    student_marks = 120
    print(check_marks(student_marks))

except InvalidMarksError as error:
    print("Custom Exception:", error)
