class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        left_most = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                # there is a height less than heights[i]
                left_most[i] = stack[-1]
            stack.append(i)
        
        stack = []
        right_most = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                # there is a height less than heights[i]
                right_most[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            left_bound = left_most[i] + 1
            right_bound = right_most[i] - 1
            max_area = max(max_area, heights[i] * (right_bound - left_bound + 1))
        return max_area
"""
[7,1,7,2,2,4]
 0 1 2 3 4 5

Area = 2 * (5 - 2 + 1)
1 * (5 - 0 + 1)

for each bar, expand left and right to check its left and right boundary
a boundary is defined if there is a height shorter than height[i]

*   *
*   *
*   *
*   *     *
*   *     *
*   * * * *
* * * * * *
"""