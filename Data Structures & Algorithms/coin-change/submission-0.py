class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
        
# [1,5,10]
# [1, 5, 5]
# dp[0] = 0
# if negative, not possible.