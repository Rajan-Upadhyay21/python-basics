# ---------------------------------------------------------
# Program: Clone Graph
# Description:
# This program clones an undirected graph using DFS.
# ---------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def clone_graph(node, clones=None):
    if node is None:
        return None

    if clones is None:
        clones = {}

    if node in clones:
        return clones[node]

    copy = Node(node.value)
    clones[node] = copy

    for neighbor in node.neighbors:
        copy.neighbors.append(clone_graph(neighbor, clones))

    return copy


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

cloned = clone_graph(node1)

print("Original node:", node1.value)
print("Cloned node:", cloned.value)
print("Neighbors of cloned node:", [n.value for n in cloned.neighbors])
