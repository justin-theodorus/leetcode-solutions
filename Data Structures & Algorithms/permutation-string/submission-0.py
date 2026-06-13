class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        expected_perm = defaultdict(int)
        for c in s1:
            expected_perm[c] += 1
        l = 0
        window = defaultdict(int)
        for r in range(len(s2)):
            window[s2[r]] += 1

            while window[s2[r]] > expected_perm[s2[r]]:
                window[s2[l]] -= 1
                l += 1
            
            if window == expected_perm:
                return True 
        return False
        
"""
s1 inside s2

all chars inside s1 is in s2
all chars must be consecutive

window must maintain a character count

shrink the window if the character count exceeds the desired
expand otherwise

s1 = "abc", s2 = "lecabee"
{a:1, b:1, c:1}
{c:1, a:1}
"""