class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check_valid(window, target):
            for key, val in target.items():
                if window[key] < val:
                    return False
            return True
        
        if not s:
            return ""
        
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        
        
        l = 0
        min_substring = [-1, -1]
        min_substring_length = float("infinity")
        window = defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1

            while check_valid(window, target):
                if (r - l + 1) < min_substring_length:
                    min_substring = [l, r]
                    min_substring_length = r - l + 1
                window[s[l]] -= 1
                l += 1
        l, r = min_substring
        return s[l:r+1] if min_substring_length != float("infinity") else ""


"""
when to expand and when to shrink?

expand while all chars in t are not in s
shrink while valid, stop once it is not valid

keep track of min length
"""
        