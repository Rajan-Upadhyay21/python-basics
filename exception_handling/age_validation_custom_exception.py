# ---------------------------------------------------------
# Program: Age Validation with Custom Exception
# Description:
# This program validates age using a custom exception.
# ---------------------------------------------------------

class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return "Age is valid."


try:
    person_age = 150
    print(validate_age(person_age))

except InvalidAgeError as error:
    print("Age Validation Error:", error)
