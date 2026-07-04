class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # populate with 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        step = 1
        while queue:
            for i in range(len(queue)):
                curRow, curCol = queue.popleft()
                for dx, dy in DIRS:
                    newRow = curRow + dx
                    newCol = curCol + dy

                    if newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited or grid[newRow][newCol] == -1:
                        continue
                    
                    visited.add((newRow, newCol))
                    grid[newRow][newCol] = step
                    queue.append((newRow, newCol))
            step += 1

"""
Multi head BFS on each 0
Process only if node != -1 and the current step is less than the value in the node

"""