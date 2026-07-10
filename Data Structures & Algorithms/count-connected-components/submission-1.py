class DSU:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n)]
        self.element = [1 for _ in range(n)]
    
    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return False
        # pi <= pj
        if self.element[pi] > self.element[pj]:
            pi, pj = pj, pi
        self.components -= 1
        self.parent[pi] = pj
        self.element[pj] += self.element[pi]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        return dsu.components