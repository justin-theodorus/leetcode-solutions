class Solution:
    def trap(self, height: List[int]) -> int:
        if (len(height) == 1):
            return 0
        
        stack = []
        ans = 0
        for h in height:
            if not stack or h <= stack[-1]:
                stack.append(h)
            else:
                if h < stack[0]:
                    tmp = []
                    while stack[-1] < h:
                        ans += h - stack.pop()
                        tmp.append(h)
                    stack += tmp
                elif h == stack[0]:
                    while stack:
                        ans += h - stack.pop()
                else:
                    new_h = stack[0]
                    while stack:
                        ans += new_h - stack.pop()
                stack.append(h)
        return ans

        

# cannot hold any water if height has 1 or 2 length
# stack
# append to stack if element is less than topmost
# if greater than topmost:
# if less than bottom of stack, pop element < than and re-insert
# if its the same, pop stack until empty
# if its greater, use the bottom stack value, then pop stack until empty

# [0,2,0,3,1,0,1,3,2,1]
# 0
# 2,0,1,1,0,1
# 3,2,1