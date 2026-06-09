class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        l = 0
        r = len(s) - 1
        while l <= r:
            while not s[l].isalnum():
                l += 1
                if l > r: return True
            while not s[r].isalnum():
                r -= 1
                if l > r: return True
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1
        return True