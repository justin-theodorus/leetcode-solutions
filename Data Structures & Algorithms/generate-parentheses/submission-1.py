class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, open, close):
            if close < open:
                # invalid
                return
            if close == 0:
                # valid
                res.append("".join(curr))
                return
            
            # pick open
            if open > 0:
                curr.append("(")
                backtrack(curr, open - 1, close)
                curr.pop()

            # pick close
            if close > 0:
                curr.append(")")
                backtrack(curr, open, close - 1)
                curr.pop()
        backtrack([], n, n)
        return res

            

"""
Well formed:
    # of ) >= # of (

For each step:
    Place a (
    Place a )

Keep track of the number of open brackets and closed brackets
"""