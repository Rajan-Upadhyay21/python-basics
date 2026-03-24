# ---------------------------------------------------------
# Program: Lowest Common Ancestor in BST
# Description:
# This program finds the lowest common ancestor of two nodes
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


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if p < root.data and q < root.data:
        return lowest_common_ancestor(root.left, p, q)

    if p > root.data and q > root.data:
        return lowest_common_ancestor(root.right, p, q)

    return root


values = [50, 30, 70, 20, 40, 60, 80]
root = None

for value in values:
    root = insert(root, value)

p = 20
q = 40

ancestor = lowest_common_ancestor(root, p, q)
print(f"Lowest Common Ancestor of {p} and {q} is:", ancestor.data)
