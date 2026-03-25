# ---------------------------------------------------------
# Program: Radix Sort
# Description:
# This program sorts non-negative integers using radix sort.
# ---------------------------------------------------------

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for number in arr:
        index = (number // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    maximum = max(arr)
    exp = 1

    while maximum // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


numbers = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original array:", numbers)
print("Sorted array:", radix_sort(numbers))
