class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReach = [False] * n
        canReach[0] = True # Starting Point

        for idx, num in enumerate(nums):
            if not canReach[idx]:
                continue
            
            for i in range(num + 1):
                if idx + i < n:
                    canReach[idx + i] = True
        
        return canReach[-1]