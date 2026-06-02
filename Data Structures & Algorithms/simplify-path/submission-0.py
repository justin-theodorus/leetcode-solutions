class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        splitted = path.split('/')
        for c in splitted:
            print(stack)
            if c == '' or c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        if not stack:
            return '/'
        return "/" + "/".join(stack)
        
