# ---------------------------------------------------------
# Program: BST Search
# Description:
# This program searches for a value in a binary search tree.
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


def search(root, target):
    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)


values = [50, 30, 70, 20, 40, 60, 80]
root = None

for value in values:
    root = insert(root, value)

target = 60

if search(root, target):
    print(f"Value {target} found in BST.")
else:
    print(f"Value {target} not found in BST.")
