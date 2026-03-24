# ---------------------------------------------------------
# Program: Median of Two Sorted Arrays
# Description:
# This introductory program finds the median by merging
# two sorted arrays.
# ---------------------------------------------------------

def find_median_sorted_arrays(nums1, nums2):
    merged = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    n = len(merged)

    if n % 2 == 1:
        return merged[n // 2]
    return (merged[n // 2 - 1] + merged[n // 2]) / 2


nums1 = [1, 3]
nums2 = [2, 4]

print("Array 1:", nums1)
print("Array 2:", nums2)
print("Median:", find_median_sorted_arrays(nums1, nums2))
