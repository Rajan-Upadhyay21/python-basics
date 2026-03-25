# ---------------------------------------------------------
# Program: Bucket Sort
# Description:
# This program sorts floating-point numbers using bucket sort.
# ---------------------------------------------------------

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for number in arr:
        index = int(number * bucket_count)
        if index == bucket_count:
            index -= 1
        buckets[index].append(number)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array


numbers = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

print("Original array:", numbers)
print("Sorted array:", bucket_sort(numbers))
