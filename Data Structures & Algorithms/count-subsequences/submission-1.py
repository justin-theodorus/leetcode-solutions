class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        nextRow = [0] * (n + 1)
        # 1 way to create an empty string from an empty string
        nextRow[-1] = 1


        for i in range(m - 1, -1, -1):
            curRow = [0] * (n + 1)
            # 1 way to form an empty string
            curRow[-1] = 1
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # skip and take current character
                    curRow[j] = nextRow[j] + nextRow[j + 1]
                else:
                    # skip current character
                    curRow[j] = nextRow[j]
            
            nextRow = curRow
        
        return nextRow[0]
"""
dp[i][j] = how many ways to form t[j:] given s[i:]
"""