class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(all, curr, idx):
            if idx >= n:
                all.append(list(curr))
                return
            
            # Choose nums[idx]
            curr.append(nums[idx])
            backtrack(all, curr, idx + 1)
            curr.pop()

            # Skip same elements
            while idx < n - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            # Skip nums[idx]
            backtrack(all, curr, idx + 1)
        nums.sort()
        all, curr = [], []
        backtrack(all, curr, 0)
        return all
"""
For an element, you can either pick or not pick
"""