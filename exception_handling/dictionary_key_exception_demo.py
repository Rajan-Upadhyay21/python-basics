# ---------------------------------------------------------
# Program: Dictionary Key Exception Demo
# Description:
# This program handles missing dictionary keys safely.
# ---------------------------------------------------------

student = {
    "name": "Rajan",
    "age": 23
}

try:
    print("Course:", student["course"])

except KeyError:
    print("Error: Requested key does not exist in dictionary.")
