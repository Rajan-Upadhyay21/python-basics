# ---------------------------------------------------------
# Program: Binary Tree Creation
# Description:
# This program demonstrates how to create a simple binary tree
# with a root node and left/right child nodes.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Binary tree created successfully.")
print("Root:", root.data)
print("Left child of root:", root.left.data)
print("Right child of root:", root.right.data)
