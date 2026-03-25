# ---------------------------------------------------------
# Program: Counting Sort
# Description:
# This program sorts non-negative integers using counting sort.
# ---------------------------------------------------------

def counting_sort(arr):
    if not arr:
        return arr

    maximum = max(arr)
    count = [0] * (maximum + 1)

    for number in arr:
        count[number] += 1

    sorted_array = []

    for value in range(len(count)):
        sorted_array.extend([value] * count[value])

    return sorted_array


numbers = [4, 2, 2, 8, 3, 3, 1]

print("Original array:", numbers)
print("Sorted array:", counting_sort(numbers))
