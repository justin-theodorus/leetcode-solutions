class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = l
            for i in range(l, r + 1):
                # find farthest reach from current range
                farthest = max(farthest, i + nums[i])
            
            l = r + 1 # min = take only 1 step from current range
            r = farthest # farthest reach
            res += 1
        return res
        
"""
For each index, track the furthest you can jump from there

Use range [l, r]
"""