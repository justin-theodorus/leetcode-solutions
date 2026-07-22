class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
        return dp[0]

            