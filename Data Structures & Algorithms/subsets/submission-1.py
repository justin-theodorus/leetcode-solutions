class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def backtrack(all, curr, idx):
            if idx >= N:
                all.append(list(curr))
                return
            
            # pick current index
            curr.append(nums[idx])
            backtrack(all, curr, idx + 1)

            # skip current index
            curr.pop()
            backtrack(all, curr, idx + 1)
        all, curr = [], []
        backtrack(all, curr, 0)
        return all

"""
For each num, we can either include or exclude
"""