# ---------------------------------------------------------
# Program: Invert Binary Tree
# Description:
# This program swaps left and right children of every node
# in a binary tree.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original tree inorder:")
inorder(root)

invert_tree(root)

print("\nInverted tree inorder:")
inorder(root)
