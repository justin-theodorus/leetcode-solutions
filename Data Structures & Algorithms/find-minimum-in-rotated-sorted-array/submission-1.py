class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]: return nums[l]

        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


"""
rotation point = when elements decrease

after rotation point = smaller set
before rotation point = larger set

Objective = find the rotation point

compare with nums[l] and nums[r]
nums[l] < nums[r] sorted, return nums[l]

[1,2,3,4,5,6]
[4,5,6,1,2,3]
[3,4,5,6,1,2]
       l   r
[6,1,2,3,4,5]

[4,5,0,1,2,3]
 l.  m     r

if mid > nums[l], we are in the larger set
    move l to mid + 1
if mid < nums[r], we are in the smaller set
    move r to mid - 1

always wanna move to the smaller set
"""
        