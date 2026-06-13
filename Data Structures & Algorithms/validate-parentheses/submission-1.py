class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        opening_tuple = ('(', '{', '[')
        stack = []
        for c in s:
            if c in opening_tuple:
                stack.append(c)
                continue
            
            if not stack or stack[-1] != pair_dict[c]:
                return False
            stack.pop()
        return True if not stack else False
            
