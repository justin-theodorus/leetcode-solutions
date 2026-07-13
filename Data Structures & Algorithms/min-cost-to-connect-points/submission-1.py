class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [float('inf')] * n
        visit = [False] * n
        edges, ans = 0, 0
        # dist[i] = min distance from cur MST to point i

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)

                if nextNode == -1 or dist[i] < dist[nextNode]:
                    # find the next node with the min edge from current MST
                    nextNode = i
            ans += dist[nextNode]
            node = nextNode
            edges += 1
        return ans
                
                