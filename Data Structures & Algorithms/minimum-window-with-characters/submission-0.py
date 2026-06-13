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
        
        if not check_valid(Counter(s), target):
            return ""
        
        l = 0
        min_substring = s
        window = defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1

            while check_valid(window, target):
                if (r - l + 1) < len(min_substring):
                    min_substring = s[l:r+1]
                window[s[l]] -= 1
                l += 1
        return min_substring


"""
when to expand and when to shrink?

expand while all chars in t are not in s
shrink while valid, stop once it is not valid

keep track of min length
"""
        