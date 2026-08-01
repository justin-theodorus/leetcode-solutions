class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # reverse row order
        matrix.reverse()

        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        

"""
n = 2
[0][0] -> [0][1]
[0][1] -> [1][1]
[1][0] -> [0][0]
[1][1] -> [1][0]
"""