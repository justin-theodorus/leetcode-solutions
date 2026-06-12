class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cur_window = defaultdict(int)
        max_substring_length = 1
        for r in range(len(s)):
            cur_window[s[r]] += 1

            while len(cur_window.keys()) > 1 and sum(cur_window.values()) - max(cur_window.values()) > k:
                cur_window[s[l]] -= 1
                if cur_window[s[l]] == 0:
                    del cur_window[s[l]]
                l += 1
            print(s[l:r+1])
            max_substring_length = max(max_substring_length, r - l + 1)
        return max_substring_length



"""
when to expand and when to shrink window?
make the window a hashmap?

expand while window has k extra elements
shrink if window has > k extra elements, until window has k extra elements
"""
        