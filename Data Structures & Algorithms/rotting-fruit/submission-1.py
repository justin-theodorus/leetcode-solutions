class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque() # (row, col)
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
        
        minute = 0
        while queue:
            for _ in range(len(queue)):
                curRow, curCol = queue.popleft()
                for dx, dy in DIRS:
                    newRow = curRow + dx
                    newCol = curCol + dy

                    if (min(newRow, newCol) < 0 or newRow == ROWS
                    or newCol == COLS or (newRow, newCol) in visited
                    or grid[newRow][newCol] == 0
                    ):
                        continue
                    visited.add((newRow, newCol))
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol))
            minute += 1
        
        for r in range(ROWS):
            if 1 in grid[r]:
                return -1
        
        return max(minute - 1, 0)

"""
Multi head BFS starting from all 2s
"""
