# ---------------------------------------------------------
# Program: Check if Tree is Balanced
# Description:
# This program checks whether a binary tree is height-balanced.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_balance(root):
    if root is None:
        return 0

    left_height = check_balance(root.left)
    if left_height == -1:
        return -1

    right_height = check_balance(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_balanced(root):
    return check_balance(root) != -1


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)

if is_balanced(root):
    print("Tree is balanced.")
else:
    print("Tree is not balanced.")
