# ---------------------------------------------------------
# Program: BST Insertion
# Description:
# This program inserts values into a binary search tree.
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


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


values = [50, 30, 70, 20, 40, 60, 80]
root = None

for value in values:
    root = insert(root, value)

print("BST inorder traversal after insertion:")
inorder(root)
