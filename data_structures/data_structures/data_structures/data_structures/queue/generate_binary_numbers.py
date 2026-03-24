# ---------------------------------------------------------
# Program: Generate Binary Numbers Using Queue
# Description:
# This program generates binary numbers from 1 to n
# using queue logic.
# ---------------------------------------------------------

from collections import deque

def generate_binary_numbers(n):
    queue = deque()
    queue.append("1")

    result = []

    for _ in range(n):
        current = queue.popleft()
        result.append(current)

        queue.append(current + "0")
        queue.append(current + "1")

    return result


n = 10
print("Binary numbers from 1 to", n, ":")
print(generate_binary_numbers(n))
