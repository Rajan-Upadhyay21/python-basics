# ---------------------------------------------------------
# Program: User Login Validation
# Description:
# This program validates username and password rules using
# exception handling.
# ---------------------------------------------------------

class InvalidLoginError(Exception):
    pass


def validate_login(username, password):
    if len(username) < 4:
        raise InvalidLoginError("Username must be at least 4 characters long.")
    if len(password) < 6:
        raise InvalidLoginError("Password must be at least 6 characters long.")
    return "Login credentials look valid."


try:
    username = "raj"
    password = "123"

    print(validate_login(username, password))

except InvalidLoginError as error:
    print("Login Error:", error)
