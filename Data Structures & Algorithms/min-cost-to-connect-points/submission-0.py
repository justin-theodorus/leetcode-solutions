class DSU:
    def __init__(self, points):
        self.components = len(points)
        self.parent = {point: point for point in points}
        self.children = {point: 1 for point in points}
    def find(self, point):
        if point != self.parent[point]:
            self.parent[point] = self.find(self.parent[point])
        return self.parent[point]
    def union(self, pointa, pointb):
        pa = self.find(pointa)
        pb = self.find(pointb)
        if pa == pb:
            return False
        
        if self.children[pa] > self.children[pb]:
            pa, pb = pb, pa
        self.parent[pa] = pb
        self.children[pb] += self.children[pa]
        self.components -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        for idx in range(len(points)):
            points[idx] = tuple(points[idx])
        dsu = DSU(points)
        pq = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pointa = points[i]
                pointb = points[j]
                heapq.heappush(pq, (abs(pointa[0] - pointb[0]) + abs(pointa[1] - pointb[1]), pointa, pointb))
        ans = 0
        while dsu.components > 1:
            cost, pointa, pointb = heapq.heappop(pq)
            if not dsu.union(pointa, pointb):
                continue
            ans += cost
        return ans