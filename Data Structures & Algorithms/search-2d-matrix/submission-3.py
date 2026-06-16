class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        lRow = 0
        rRow = ROWS - 1
        targetRow = -1

        while lRow <= rRow:
            midRow = lRow + ((rRow - lRow) // 2)
            if matrix[midRow][0] == target or matrix[midRow][-1] == target:
                return True 
            elif matrix[midRow][0] < target < matrix[midRow][-1]:
                targetRow = midRow
                break
            elif matrix[midRow][0] > target:
                rRow = midRow - 1
            else:
                lRow = midRow + 1

        if targetRow == -1: return False
        
        lCol = 0
        rCol = COLS - 1
        while lCol <= rCol:
            midCol = lCol + ((rCol - lCol) // 2)
            if matrix[targetRow][midCol] == target:
                return True
            elif matrix[targetRow][midCol] < target:
                lCol = midCol + 1
            else:
                rCol = midCol - 1
        return False
"""
find row first? then find col in that row
"""