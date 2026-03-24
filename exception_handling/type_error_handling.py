# ---------------------------------------------------------
# Program: Type Error Handling
# Description:
# This program handles invalid operations between different
# incompatible data types.
# ---------------------------------------------------------

try:
    result = "10" + 5
    print(result)

except TypeError:
    print("Error: Cannot add string and integer directly.")
