class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            queue.append([r, c])

        # populate with 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        step = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = step
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            step += 1

"""
Multi head BFS on each 0
Process only if node != -1 and the current step is less than the value in the node

"""