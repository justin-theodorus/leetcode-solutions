class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curTotal = 0
        for num in nums:
            curTotal += num
            res = max(res, curTotal)
            if curTotal < 0:
                curTotal = 0
            
        
        return res