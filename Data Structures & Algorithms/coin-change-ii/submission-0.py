class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
            # always 1 way to get a target amount of 0
        
        for i in range(n - 1, -1, -1):
            for j in range(amount + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]
        
        return dp[0][amount]
"""
dp[i][a] = number of ways to get target a from coins[i:]
Goal = dp[0][amount]

dp[i][a] = dp[i + 1][a] (skip) + dp[i][a - coins[i]] (take)
"""