class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        def backtrack(all, curr, idx, target):
            if idx >= N or target < 0:
                return
            if target == 0:
                all.append(list(curr))
                return
            
            # Take
            curr.append(nums[idx])
            backtrack(all, curr, idx, target - nums[idx])
            curr.pop()

            # Not Take
            backtrack(all, curr, idx + 1, target)
        all, curr = [], []
        backtrack(all, curr, 0, target)
        return all

"""
For each step:
    Take the current num, decrease target by num
        Continue from the same idx
        Continue from the next num (idx + 1)
    Skip the current num, target not changed
        Continue from the next num (idx + 1)
"""