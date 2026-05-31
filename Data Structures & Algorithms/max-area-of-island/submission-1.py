class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(grid, r+1, c) + dfs(grid, r-1, c) + dfs(grid, r, c+1) + dfs(grid, r, c-1)
            

        max_size = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_size = max(max_size, dfs(grid, r, c))
        return max_size


# 1. Iterate through cell, find 1
# 2. Perform DFS on that 'island'. For each cell visited, change the value to 0
# so that it won't be visited again, and keep track of the number of 1s seen so far.
# 3. Keep track of the max size of all islands and return the answer