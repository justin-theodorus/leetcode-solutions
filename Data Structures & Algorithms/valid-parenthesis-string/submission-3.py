class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                # ) always decrease ( count
                low = max(0, low - 1)
                high -= 1
            else:
                low = max(0, low - 1) # can be )
                high += 1 # can be (
            
            if high < 0:
                # too many )
                return False
                
        return low == 0
"""
Track the minimum/maximum number of unmatched ( 
"""