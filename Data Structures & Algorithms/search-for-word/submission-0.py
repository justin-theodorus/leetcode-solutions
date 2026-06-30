class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c, visited, idx):
            if idx >= n:
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[idx]:
                return False
            
            visited.add((r, c))
            for x, y in DIRS:
                newRow = r + x
                newCol = c + y
                if (newRow, newCol) not in visited and dfs(newRow, newCol, visited, idx + 1):
                    return True
            visited.discard((r,c))

            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, set(), 0):
                    return True
        return False

"""
DFS on every character that is equal to word[0]
"""