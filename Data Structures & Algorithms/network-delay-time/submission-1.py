class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((t, v))
        
        pq = [(0, k)] # min-heap
        visit = set()

        while pq:
            curTime, curNode = heapq.heappop(pq)  
            if curNode in visit:
                continue
            visit.add(curNode)
            if len(visit) == n:
                return curTime
            for t, v in adjList[curNode]:
                newTime = curTime + t
                heapq.heappush(pq, (newTime, v))
        return -1

"""
Objective: visit all nodes with the minimum time
k = starting node
times = directed edges with weights

Always pick the edge with the smallest time from the current node (Djikstra)
"""