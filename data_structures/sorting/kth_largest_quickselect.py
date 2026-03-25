# ---------------------------------------------------------
# Program: Kth Largest Element using Quickselect
# Description:
# This program finds the kth largest element using
# the quickselect technique.
# ---------------------------------------------------------

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]

    greater = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    smaller = [x for x in arr if x < pivot]

    if k <= len(greater):
        return quickselect(greater, k)
    elif k <= len(greater) + len(equal):
        return pivot
    else:
        return quickselect(smaller, k - len(greater) - len(equal))


numbers = [3, 2, 1, 5, 6, 4]
k = 2

print("Array:", numbers)
print(f"{k}nd largest element:", quickselect(numbers, k))
