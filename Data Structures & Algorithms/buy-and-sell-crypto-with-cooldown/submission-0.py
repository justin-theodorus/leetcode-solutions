class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1_buy, dp1_sell, dp2_buy = 0, 0, 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)

            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = dp_buy, dp_sell
        return dp1_buy

"""
2 states on each day = can buy or cannot buy (sell)
dp1_buy = best profit if allowed to buy on the next day
dp1_sell = best profit if allowed to sell on the next day
dp2_buy = best profit if allowed to buy 2 days ahead

If buy allowed:
    - buy today and sell on future days (dp1_sell)
    - Skip buying today (dp1_buy)
If buy not allowed (holding):
    - Sell today, cooldown tmrw, and able to buy again 2 days (dp2_buy)
    - Skip selling today (dp1_sell)
"""
