# ---------------------------------------------------------
# Program: API Response Validator
# Description:
# This program simulates validation of an API response
# and raises exceptions when required fields are missing.
# ---------------------------------------------------------

class APIValidationError(Exception):
    pass


def validate_response(response):
    required_keys = ["status", "data", "message"]

    for key in required_keys:
        if key not in response:
            raise APIValidationError(f"Missing required key: {key}")

    if response["status"] != 200:
        raise APIValidationError("API returned unsuccessful status code.")

    return "API response is valid."


try:
    api_response = {
        "status": 200,
        "data": {"id": 101, "name": "Rajan"}
    }

    result = validate_response(api_response)
    print(result)

except APIValidationError as error:
    print("API Validation Error:", error)

except Exception as error:
    print("Unexpected Error:", error)

finally:
    print("API validation completed.")
