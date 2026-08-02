class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zeroRow, zeroCol = set(), set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] != 0:
                    continue
                zeroRow.add(r)
                zeroCol.add(c)
        
        for r in zeroRow:
            for c in range(n):
                matrix[r][c] = 0
        
        for c in zeroCol:
            for r in range(m):
                matrix[r][c] = 0



        