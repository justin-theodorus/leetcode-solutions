class DSU:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n + 1)]
        self.children = [1 for _ in range(n + 1)]
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.children[pa] > self.children[pb]:
            pa, pb = pb, pa
        
        self.components -= 1
        self.parent[pa] = pb
        self.children[pb] += self.children[pa]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for edge in edges:
            if dsu.components == 1 or not dsu.union(edge[0], edge[1]):
                return edge
"""
Build an MST from edges
"""