# ---------------------------------------------------------
# Program: Huffman Coding Intro
# Description:
# This program builds Huffman codes for characters
# using a greedy approach with a priority queue.
# ---------------------------------------------------------

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)


char_frequency = {
    "a": 5,
    "b": 9,
    "c": 12,
    "d": 13,
    "e": 16,
    "f": 45
}

root = build_huffman_tree(char_frequency)
codes = {}
generate_codes(root, "", codes)

print("Huffman Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")
