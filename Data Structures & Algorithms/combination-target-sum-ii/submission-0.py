class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        def backtrack(all, curr, idx, target):
            if target == 0:
                # valid combination
                all.append(list(curr))
                return
            if target < 0 or idx >= n:
                # invalid combination
                return
            
            # choose current element
            curr.append(candidates[idx])
            backtrack(all, curr, idx + 1, target - candidates[idx])
            curr.pop()

            # skip same elements after
            while idx + 1 < n and candidates[idx] == candidates[idx + 1]:
                idx += 1

            # skip current element
            backtrack(all, curr, idx + 1, target)
        
        all, curr = [], []
        candidates.sort()
        backtrack(all, curr, 0, target)
        return all


"""
Each element from candidates may be chosen at most once 
within a combination. 

Return all unique combinations that sum to target

must always increment index
Each element can be chosen or not chosen

How to not include duplicates?
[1,2,2,2,3] target = 5

choosing [1,2,2] with 2 from index 1 and 2 and
2 from index 1 and 3 is the same

Sort first and skip elements that are the same as its prev?
 
[1,2,2,4,5,6,9] target = 8
Assume we choose 1, then we choose 2 (index 1)
After backtracking is completed, we skip the next 2 (index 2),
else it will be running backtracking on target = 5 again (8 - 1 - 2)
and [1,2,5] will be included twice
"""