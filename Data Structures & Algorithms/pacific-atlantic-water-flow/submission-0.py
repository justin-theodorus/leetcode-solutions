class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacificSource = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atlanticSource = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                for _ in range(len(q)):
                    curRow, curCol = q.popleft()
                    ocean[curRow][curCol] = True

                    for dx, dy in DIRS:
                        newRow = curRow + dx
                        newCol = curCol + dy
                        if (newRow in range(ROWS) and newCol in range(COLS)
                            and not ocean[newRow][newCol] 
                            and heights[newRow][newCol] >= heights[curRow][curCol]
                        ):
                            q.append((newRow, newCol))


        pacific = []
        atlantic = []

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))
        
        bfs(pacific, pacificSource)
        bfs(atlantic, atlanticSource)

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacificSource[r][c] and atlanticSource[r][c]:
                    ans.append([r, c])
        return ans


"""
water can only flow if path is decreasing

(0, COLS - 1) and (ROWS - 1, 0) are guaranteed

Can reuse coordinates already marked as answers
If a cell can reach those coordiante, it is an answer too

Need to keep track of path.
Once a cell is an answer, all the coords in the path is also an answer

Pacific: r = 0 or c = 0
Atlantic: r = ROWS - 1 or c = COLS - 1

Multi source BFS starting from the ocean edges (both pacific and atlantic)
"""