class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


"""
[1,2,1,2,1,1,1]
 0 0 1 2 2 3 3  4

Target index = N
N = len(cost)

min_step at index i = min(min_step[i - 1] + cost[i - 1], min_step[i - 2] + cost[i - 2])
"""