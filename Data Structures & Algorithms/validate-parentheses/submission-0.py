class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for sym in s:
            if sym == '(' or sym == '{' or sym == '[':
                stack.append(sym)
            else:
                if sym == ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                elif sym == '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                elif sym == ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
        if len(stack) != 0:
            return False
        
        return True