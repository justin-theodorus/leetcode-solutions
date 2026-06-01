class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        i = 0
        cur = 0
        while i < len(nums):
            while count[cur] == 0:
                cur += 1
            nums[i] = cur
            count[cur] -= 1
            i += 1


# 0 1 2
# use a dictionary to track the count of 0, 1, and 2
# do a for loop from 0 to 2 (inclusive), assume index i
# nums[i] = 0 1 or 2 (stop when the count reaches 0)
        