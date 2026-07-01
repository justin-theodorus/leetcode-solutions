class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans, curr = [], []
        def is_palindrome(s, l ,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        def backtrack(idx):
            if idx >= n:
                ans.append(list(curr))
            for j in range(idx, n):
                if is_palindrome(s, idx, j):
                    curr.append(s[idx : j + 1])
                    backtrack(j + 1)
                    curr.pop()
        
        backtrack(0)
        return ans

        
"""
Append if palindrome (choose)
Try to partition the idx + 1
Pop (backtrack)
"""