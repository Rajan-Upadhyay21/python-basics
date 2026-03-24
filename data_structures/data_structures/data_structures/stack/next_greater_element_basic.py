# ---------------------------------------------------------
# Program: Next Greater Element
# Description:
# This program finds the next greater element for each array
# value using a stack.
# ---------------------------------------------------------

def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


numbers = [4, 5, 2, 10, 8]

print("Array:", numbers)
print("Next greater elements:", next_greater_element(numbers))
