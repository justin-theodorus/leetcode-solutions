class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_smallest = prices[0]
        for price in prices:
            if price < cur_smallest:
                cur_smallest = price
            diff = price - cur_smallest
            max_profit = max(max_profit, diff)
        return max_profit


"""
iterate through
track cur_smallest
for each > cur_smallest, take the difference with cur_smallest
return max difference
"""