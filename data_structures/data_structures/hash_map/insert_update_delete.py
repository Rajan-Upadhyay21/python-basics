# ---------------------------------------------------------
# Program: Insert, Update, and Delete in Hash Map
# Description:
# This program demonstrates insertion, update, and deletion
# of key-value pairs in a dictionary.
# ---------------------------------------------------------

employee = {}

# Insert values
employee["name"] = "Rajan"
employee["role"] = "AI Engineer"
employee["salary"] = 85000

print("After insertion:")
print(employee)

# Update value
employee["salary"] = 90000

print("\nAfter update:")
print(employee)

# Delete value
del employee["role"]

print("\nAfter deletion:")
print(employee)
