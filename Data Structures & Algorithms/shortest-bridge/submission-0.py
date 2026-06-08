class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island_coords = set()
        ROW = len(grid)
        COL = len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0,1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0 or (r,c) in island_coords:
                return
            island_coords.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        found = False
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found: break
        
        q = deque(list(island_coords))
        visited = set(island_coords)
        level = 0
        while q:
            for i in range(len(q)):
                cur_row, cur_col = q.popleft()
                # print(cur_row, cur_col)
                for dir in DIRS:
                    new_row = cur_row + dir[0]
                    new_col = cur_col + dir[1]

                    if new_row < 0 or new_col < 0 or new_row >= ROW or new_col >= COL or (new_row,new_col) in visited:
                        continue
                    if grid[new_row][new_col] == 1:
                        return level
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col))
            level += 1
        return level
                    
                


"""
DFS on an island, store all coords of the 1
Multi Source BFS on each 1 until another 1 is found
If its not in the seen coords (ori island), return step
"""