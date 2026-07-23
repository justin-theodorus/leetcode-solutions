class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n
        curRow = [1]

        for i in range(1, m):
            for j in range(1, n):
                curRow.append(curRow[j - 1] + prevRow[j])
            prevRow = curRow
            curRow = [1]
        return prevRow[-1]