class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        nextRow = [i for i in range(n, -1, -1)]
        # operations to form an empty string given word1[i:]

        for i in range(m - 1, -1, -1):
            curRow = [0] * (n + 1)
            # m - i operations to form an empty string given word1[i:]
            curRow[-1] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    curRow[j] = nextRow[j + 1]
                else:
                    # delete, insert, or replace
                    curRow[j] = 1 + min(
                        nextRow[j], 
                        curRow[j + 1], 
                        nextRow[j + 1])
            
            nextRow = curRow
        
        return nextRow[0]

        
            
            
"""
dp[i][j] = Number of operations to form word2[j:] given word1[i:]

If word1[i] == word2[j]: (no operation)
    dp[i][j] = dp[i + 1][j + 1]
else:
    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
"""