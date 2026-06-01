class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(all, curr, open, close, n):
            if (close > open or open > n or close > n):
                return
            if (open == n and close == n):
                all.append("".join(curr))
                return
            
            curr.append("(")
            backtrack(all, curr, open + 1, close, n)
            curr.pop()

            curr.append(")")
            backtrack(all, curr, open, close + 1, n)
            curr.pop()

            return
        
        all = []
        curr = []
        backtrack(all, curr, 0, 0, n)
        return all
            

# there are 2 choices for each step, either "(" or ")"
# invalid if:
#   close > open
#   open > n
#   close > n