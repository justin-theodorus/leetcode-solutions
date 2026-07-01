class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z'),
        }
        n = len(digits)
        ans = []
        curr = []

        def backtrack(idx):
            if idx == n:
                ans.append("".join(curr))
                return
            
            for letter in digitMap[digits[idx]]:
                curr.append(letter)
                backtrack(idx + 1)
                curr.pop()
            return
        backtrack(0)
        return ans
"""
1 digit = 3-4 characters

All unique combinations of these characters

For every digit, we
    Pick a character from one of its choices
    Continue to the next digit
    Pop and try a different character
"""