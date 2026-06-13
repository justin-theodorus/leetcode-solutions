class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = defaultdict(int)
        # original window
        for i in range(k-1):
            window[nums[i]] += 1

        ans = []

        l = 0
        for r in range(k-1, len(nums)):
            window[nums[r]] += 1
            ans.append(max(window))

            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                del window[nums[l]]
            l += 1
        return ans


"""
track the MAX value inside a window and track its index

If the MAX value goes out of window bound, there needs to be a way to know the NEXT MAX value and index

the window can be a dict/hashmap?
[1,2,0,1,0,2,6]
       l   r
"""
        