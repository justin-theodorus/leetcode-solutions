class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])
        def check_row():
            seen = set()
            for r in range(ROW):
                for c in range(COL):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])
                seen = set()
            return True

        def check_col():
            seen = set()
            for c in range(COL):
                for r in range(ROW):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])
                seen = set()
            return True

        def check_square(r, c):
            seen = set()
            for row in range(r, r + 3):
                for col in range(c, c + 3):
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
            return True
        
        if not check_row() or not check_col():
            return False
        for r in range(0, ROW, 3):
            for c in range(0, COL, 3):
                if not check_square(r,c):
                    return False 
        return True