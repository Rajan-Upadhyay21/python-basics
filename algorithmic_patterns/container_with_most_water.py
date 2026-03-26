# ---------------------------------------------------------
# Program: Container With Most Water
# Description:
# This program finds the maximum water container
# using the two pointers pattern.
# ---------------------------------------------------------

def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        best = max(best, width * current_height)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print("Maximum area:", max_area(height))
