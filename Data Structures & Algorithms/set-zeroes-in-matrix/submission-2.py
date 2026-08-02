class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        # check if first row must be zeroed
        firstRowZero = False
        # matrix[0][0] = track if first column needs to be zeroed

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # mark a row must be 0
                    matrix[0][c] = 0

                    if r > 0:
                        # mark a col must be 0
                        matrix[r][0] = 0
                    else:
                        firstRowZero = True
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
        
        if firstRowZero:
            for c in range(n):
                matrix[0][c] = 0

        