class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

"""
slow and fast pointer

index -> index

an index is pointing to the value of the current index
there will be 2 indices pointing to the same index -> cycle
slow == fast cycle detected

have another slow2, advance until slow == slow2 -> index where cycle happens

"""