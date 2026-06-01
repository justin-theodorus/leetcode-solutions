class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, remaining, start):
            if remaining == 0:
                result.append(curr[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(curr, remaining - nums[i], i)
                curr.pop()
        
        result = []
        backtrack([], target, 0)
        return result