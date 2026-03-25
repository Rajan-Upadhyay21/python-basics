# ---------------------------------------------------------
# Program: Selection Sort
# Description:
# This program sorts an array using selection sort.
# It repeatedly selects the smallest element and
# places it in the correct position.
# ---------------------------------------------------------

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


numbers = [29, 10, 14, 37, 13]

print("Original array:", numbers)
print("Sorted array:", selection_sort(numbers))
