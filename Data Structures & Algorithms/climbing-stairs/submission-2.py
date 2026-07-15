class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = [0 for _ in range(n + 1)]
        memo[1], memo[2] = 1, 2

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[-1]
"""
only 1 OR 2 steps at a time

Sum of steps = n

climbStairs(1) = 1
    1

climbStairs(2) = 2
    1 + 1
    2

climbStairs(3) = 3 = climStairs(1) + climbStairs(2)
    1 + 1 + 1
    2 + 1
    1 + 2

climbStairs(4) = climbStairs(2) + climbStairs(3) = 5
    1 + 1 + 2
    2 + 2
    1 + 1 + 1 + 1
    2 + 1 + 1
    1 + 2 + 1
"""