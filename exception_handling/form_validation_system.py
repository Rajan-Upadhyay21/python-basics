# ---------------------------------------------------------
# Program: Form Validation System
# Description:
# This program validates form inputs like name, age,
# and email using custom exceptions.
# ---------------------------------------------------------

class ValidationError(Exception):
    pass


def validate_name(name):
    if not name.strip():
        raise ValidationError("Name cannot be empty.")

def validate_age(age):
    if age < 18 or age > 100:
        raise ValidationError("Age must be between 18 and 100.")

def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email format.")


try:
    user_name = "Rajan"
    user_age = 23
    user_email = "rajanupadhyay2121@gmail.com"

    validate_name(user_name)
    validate_age(user_age)
    validate_email(user_email)

    print("All form fields are valid.")

except ValidationError as error:
    print("Form Validation Error:", error)

except Exception as error:
    print("Unexpected Error:", error)

finally:
    print("Form validation process completed.")
