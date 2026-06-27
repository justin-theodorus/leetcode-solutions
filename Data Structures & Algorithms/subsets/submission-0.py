class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(all, curr, idx):
            if idx >= len(nums):
                all.append(list(curr))
                return
            
            # pick current index
            curr.append(nums[idx])
            backtrack(all, curr, idx + 1)

            # skip current index
            curr.pop()
            backtrack(all, curr, idx + 1)
        all, curr = [], []
        idx = 0
        backtrack(all, curr, idx)
        return all

"""
For each num, we can either include or exclude
"""