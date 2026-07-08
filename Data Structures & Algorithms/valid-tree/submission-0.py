class DSU:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
    
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            # already same component = cycle if try to union
            return False
        
        # merge the smaller size to the bigger one
        if self.size[pi] < self.size[pj]:
            pi, pj = pj, pi
        self.components -= 1
        self.parent[pj] = pi
        self.size[pi] += self.size[pj]
        return True
    
    def componentCount(self):
        return self.components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for a, b in edges:
            if not dsu.union(a, b):
                return False
        # connected = 1 component
        return True if dsu.componentCount() == 1 else False
        

"""
valid tree = acyclic and connected

"""