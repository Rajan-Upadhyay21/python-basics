# ---------------------------------------------------------
# Program: Count Leaf Nodes
# Description:
# This program counts the number of leaf nodes in a binary tree.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_leaf_nodes(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Number of leaf nodes:", count_leaf_nodes(root))
