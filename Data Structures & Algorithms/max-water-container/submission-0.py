class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while (l < r):
            cur_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, cur_area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area


"""
Area = min(height[l], height[r]) * (r - l)

move the min pointer
"""
        