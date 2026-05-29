class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            if (r, c) in visited or grid[r][c] == 0:
                return
            
            visited.add((r,c))
            curr_island.add((r - origin_row, c - origin_col))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        unique = set()
        for r in range(row):
            for c in range(col):
                curr_island = set()
                origin_row = r
                origin_col = c
                dfs(r, c)
                if curr_island:
                    unique.add(frozenset(curr_island))
        return len(unique)

        
