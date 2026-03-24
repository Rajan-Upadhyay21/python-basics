# ---------------------------------------------------------
# Program: Linear Search
# Description:
# This program searches for a target element in an array.
# ---------------------------------------------------------

arr = [5, 12, 18, 25, 30, 42]
target = 25

found = False

for index in range(len(arr)):
    if arr[index] == target:
        print("Element found at index:", index)
        found = True
        break

if not found:
    print("Element not found.")
