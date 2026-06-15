class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # (val, idx)
        for idx, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                _, i = stack.pop()
                ans[i] = idx - i
            stack.append((tmp, idx))
        return ans
            
"""
[30,38,30,36,35,40,28]
idx = 6
[(40,5), (28,6)]
[1,4,1,2,1,0,0]
"""