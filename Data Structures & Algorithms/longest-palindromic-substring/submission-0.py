class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIdx, resLen = 0, 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                
                    # update longest
                    if resLen < j - i + 1:
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx : resIdx + resLen]
"""
dp[i][j] = s[i...j] is a palindrome

If j - i <= 2 (len less than eq 3), its palindrome
dp[i][j] True if dp[i + 1][j - 1] True
"""