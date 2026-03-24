# ---------------------------------------------------------
# Program: Majority Element
# Description:
# This program finds the majority element using a hash map.
# ---------------------------------------------------------

def majority_element(nums):
    counts = {}
    threshold = len(nums) // 2

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > threshold:
            return num

    return None


numbers = [2, 2, 1, 1, 2, 2, 2]

print("Numbers:", numbers)
print("Majority element:", majority_element(numbers))
