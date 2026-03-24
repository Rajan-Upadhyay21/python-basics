# ---------------------------------------------------------
# Program: Find Min and Max in BST
# Description:
# This program finds the minimum and maximum value
# in a binary search tree.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.data


def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.data


values = [50, 30, 70, 20, 40, 60, 80]
root = None

for value in values:
    root = insert(root, value)

print("Minimum value in BST:", find_min(root))
print("Maximum value in BST:", find_max(root))
