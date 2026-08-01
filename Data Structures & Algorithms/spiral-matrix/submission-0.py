class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # right -> down -> left -> up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # index 0 = steps left horizontally
        # index 1 = steps left vertically
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c = 0, -1 # starting coords
        d = 0 # direction

        while steps[d & 1]:
            # d & 1 checks with steps to use (hori/verti)
            for i in range(steps[d & 1]):
                r += dirs[d][0]
                c += dirs[d][1]
                res.append(matrix[r][c])
            
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res
"""
At every direction, the steps allowed decrease by 1
"""