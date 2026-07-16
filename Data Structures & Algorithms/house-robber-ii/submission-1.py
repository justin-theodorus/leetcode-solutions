class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        # either select the first house, or don't
        
    def helper(self, nums):

        rob1 = 0 # max money until house i -2
        rob2 = 0 # max money until house i - 1

        for num in nums:
            newRob = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2