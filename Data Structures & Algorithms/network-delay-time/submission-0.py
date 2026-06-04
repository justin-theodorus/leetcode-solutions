class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # source = k
        adj = {i: [] for i in range(1, n+1)}
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))
        
        min_heap = [(0, k)]
        min_dist = [-1 for _ in range(n+1)]
        min_dist[0] = 0
        # 0 is not used
        # min_dist[k] = 0 # start is 0 in time

        while min_heap:
            cur_time, node = heapq.heappop(min_heap)
            if min_dist[node] != -1:
                continue
            min_dist[node] = cur_time
            for time, neighbor in adj[node]:
                new_time = cur_time + time
                heapq.heappush(min_heap, (new_time, neighbor))
        
        if -1 in set(min_dist):
            return -1
        return max(min_dist)
            


"""
1   2   3   4
0   1  2  -1


[(4,4), (3, 4)]
"""

        