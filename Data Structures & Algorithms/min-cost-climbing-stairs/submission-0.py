class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        N = len(cost)
        min_cost = [0 for _ in range(N + 1)]
        # starting index can be 0 and 1
        idx = 2
        while idx <= N:
            min_cost[idx] = min(min_cost[idx - 1] + cost[idx - 1], min_cost[idx - 2] + cost[idx - 2])
            idx += 1
        return min_cost[-1]


"""
[1,2,1,2,1,1,1]
 0 0 1 2 2 3 3  4

Target index = N
N = len(cost)

min_step at index i = min(min_step[i - 1] + cost[i - 1], min_step[i - 2] + cost[i - 2])
"""