# ---------------------------------------------------------
# Program: Tree Traversals (DFS)
# Description:
# This program demonstrates preorder, inorder, and postorder
# traversal of a binary tree using recursion.
# ---------------------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder traversal:")
preorder(root)

print("\n\nInorder traversal:")
inorder(root)

print("\n\nPostorder traversal:")
postorder(root)
