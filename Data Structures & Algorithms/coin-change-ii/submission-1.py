class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1

            for j in range(amount + 1):
                nextDp[j] = dp[j] # Skip
                if j >= coins[i]:
                    nextDp[j] += nextDp[j - coins[i]] # Take
            
            dp = nextDp
        return dp[-1]
"""
dp[i][a] = number of ways to get target a from coins[i:]
Goal = dp[0][amount]

dp[i][a] = dp[i + 1][a] (skip) + dp[i][a - coins[i]] (take)
"""