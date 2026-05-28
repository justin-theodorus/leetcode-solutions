class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:

            return self.climbStairs(n-1) + self.climbStairs(n-2)
        