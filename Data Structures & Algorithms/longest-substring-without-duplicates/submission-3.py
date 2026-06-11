class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = r = 0
        window = set()
        max_len = 1
        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
            else:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                l += 1
            max_len = max(max_len, len(window))
        return max_len
        

"""
sliding window

iterate through s using r
if char has not been seen, continue the r pointer
else, move the left pointer until c is no longer in the window

xzyzxyz
  l
    r

seen = [z, y, x]
"""