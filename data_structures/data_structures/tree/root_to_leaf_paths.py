# ---------------------------------------------------------
# Program: Root to Leaf Paths
# Description:
# This program prints all root-to-leaf paths in a binary tree.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_paths(root, path):
    if root is None:
        return

    path.append(root.data)

    if root.left is None and root.right is None:
        print(path)
    else:
        print_paths(root.left, path)
        print_paths(root.right, path)

    path.pop()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Root to leaf paths:")
print_paths(root, [])
