class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        path = set()
        pq = [(grid[0][0],0, 0)]
        DIRS = [(0,1), (0,-1), (1,0), (-1,0)]
        # end = (n-1, n-1)

        while pq:
            val, row, col = heapq.heappop(pq)
            if val in path:
                continue
            path.add(val)
            if row == ROW - 1 and col == COL - 1:
                break

            for dir_x, dir_y in DIRS:
                new_row = row + dir_x
                new_col = col + dir_y

                if new_row < 0 or new_col < 0 or new_row >= ROW or new_col >= COL:
                    continue
                new_val = grid[new_row][new_col]
                heapq.heappush(pq, (new_val, new_row, new_col))
        return max(path)




"""
path = [0, 1, 2, 4, 8, 3, 5, 7, 6]
[(9, 1, 0), (14, 1, 1), (10,0,3), (13,2,3), (15,3,4), (7,4,3)]
"""
        