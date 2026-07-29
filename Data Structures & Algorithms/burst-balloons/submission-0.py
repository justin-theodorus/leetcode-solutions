class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n+2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                # i is the last baloon popped between [l,r]
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]
        
"""
dp[l][r] represent the maximum coins we can collect 
by bursting all balloons from index l to r (inclusive)

Let i be the last baloon popped in range [l ,r]
By the time i is popped, baloons from [l, i - 1] and [i + 1, r] is gone.
dp[l][r] = nums[l - 1] * nums[i] * nums[r + 1] +  dp[l, i - 1] + dp[i + 1, r]

[l, i - 1] and [i + 1, r] becomes a subproblem

Answer = dp[1][n]
"""