class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set([(0,0)])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(grid[0][0], 0, 0)]

        while pq:
            for _ in range(len(pq)):
                curTime, r, c = heapq.heappop(pq)

                if r == N - 1 and c == N - 1:
                    return curTime
                
                for dx, dy in DIRS:
                    newR = r + dx
                    newC = c + dy
                    if newR < 0 or newC < 0 or newR >= N or newC >= N or (newR, newC) in visit:
                        continue
                    
                    visit.add((newR, newC))
                    heapq.heappush(pq, (max(curTime, grid[newR][newC]), newR, newC))
                    
