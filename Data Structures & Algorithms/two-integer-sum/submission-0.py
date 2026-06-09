class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val to idx
        for idx, num in enumerate(nums):
            if (target-num) not in seen:
                seen[num] = idx
            else:
                return [seen[target-num], idx]