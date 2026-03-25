# ---------------------------------------------------------
# Program: Sort Colors (Dutch National Flag)
# Description:
# This program sorts an array containing only 0s, 1s, and 2s.
# ---------------------------------------------------------

def sort_colors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


numbers = [2, 0, 2, 1, 1, 0]

print("Original array:", numbers)
print("Sorted array:", sort_colors(numbers))
