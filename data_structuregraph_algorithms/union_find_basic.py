# ---------------------------------------------------------
# Program: Union-Find Basic
# Description:
# This program demonstrates the disjoint set union
# data structure with union and find operations.
# ---------------------------------------------------------

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(6)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print("Are 0 and 2 connected?", uf.connected(0, 2))
print("Are 0 and 4 connected?", uf.connected(0, 4))
