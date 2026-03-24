# ---------------------------------------------------------
# Program: Key Lookup in Hash Map
# Description:
# This program demonstrates checking whether a key exists
# in a dictionary.
# ---------------------------------------------------------

product = {
    "id": 101,
    "name": "Laptop",
    "price": 1200
}

search_key = "price"

if search_key in product:
    print(f"Key '{search_key}' found with value:", product[search_key])
else:
    print(f"Key '{search_key}' not found.")
