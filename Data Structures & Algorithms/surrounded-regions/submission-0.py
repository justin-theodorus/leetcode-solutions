class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        surrounded = [[True for _ in range(COLS)] for _ in range(ROWS)]
        def dfs(row, col):
            if row in range(ROWS) and col in range(COLS) and surrounded[row][col] and board[row][col] == "O":
                surrounded[row][col] = False
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O" and surrounded[r][c]:
                    board[r][c] = "X"

"""
Find "islands" of "O"s, where no "O"s are touching the edge

edge:
    r = 0 or
    c = 0 or
    r = ROWS - 1 or
    c = COLS - 1 or

Iterate through each cell touching the edges
If we found "O", do DFS to mark all connected "O" as False (not surrounded)
Repeat

Iterate through all cells
If cells are marked as True (surrounded) and is "O", change to "X"
"""