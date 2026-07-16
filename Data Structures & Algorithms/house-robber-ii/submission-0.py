class Solution:
    def robUsual(self, nums):
        if len(nums) <= 2:
            return max(nums)
        take, skip = nums[-1], max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, -1, -1):
            tmp = skip
            skip = max(nums[i] + take, skip)
            take = tmp
        return skip

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(nums[0] + self.robUsual(nums[2:-1]), self.robUsual(nums[1:]))
        
