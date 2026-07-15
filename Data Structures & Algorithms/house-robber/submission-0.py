class Solution:
    def rob(self, nums: List[int]) -> int:
        take, skip = 0, nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            tmp = skip
            skip = max(take + nums[i], skip)
            take = tmp
        return skip
"""
At each house, we can either pick, or not pick

[2,9,8,3,6]
rob([2,9,8,3,6]) = 
    2 + rob([8,3,6]) TAKE OR
    rob([9,3,8,6]) SKIP

rob([9,8,3,6]) = 
    9 + rob([3,6]) TAKE OR
    rob([8,3,6]) SKIP

rob([8,3,6]) =
    8 + rob([6]) TAKE OR
    rob([3,6]) SKIP

rob([3, 6]) = 6
    3 + rob([]) (TAKE) OR
    rob([6]) (SKIP)

rob([6]) = 6 (BASE CASE)
    6 + rob([]) 

rob([]) = 0 (BASE CASE)

Every iteration backwards:
    Current value becomes next SKIP value
    Current SKIP value becomes next TAKE value

"""