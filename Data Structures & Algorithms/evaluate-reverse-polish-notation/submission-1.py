class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(["+", "*", "-", "/"])
        for token in tokens:
            if not stack or token not in op:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
        return stack[0]