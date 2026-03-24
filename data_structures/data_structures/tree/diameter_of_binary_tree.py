# ---------------------------------------------------------
# Program: Diameter of Binary Tree
# Description:
# This program finds the diameter of a binary tree.
# Diameter means the length of the longest path between
# any two nodes.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter_of_tree(root):
    diameter = [0]

    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        diameter[0] = max(diameter[0], left_height + right_height)

        return max(left_height, right_height) + 1

    height(root)
    return diameter[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter of binary tree:", diameter_of_tree(root))
