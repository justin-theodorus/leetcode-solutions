class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [list(nums)]
        
        all = []
        first = nums[0]
        for perm in self.permute(nums[1:]):
            len_perm = len(perm)
            for idx in range(len_perm + 1):
                curr = perm[:idx] + [first] + perm[idx:]
                all.append(curr)
        return all