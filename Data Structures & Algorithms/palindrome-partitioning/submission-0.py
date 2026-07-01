class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def is_palindrome(substr):
            l = 0
            r = len(substr) - 1
            while l <= r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        def backtrack(curr, idx):
            # curr is a list of a list of chars
            if idx == n:
                for i in range(len(curr)):
                    if not is_palindrome(curr[i]):
                        return
                tmp = ["".join(curr[i]) for i in range(len(curr))]
                ans.append(list(tmp))
                return
            
            # Current character is part of last substring
            if curr:
                curr[-1].append(s[idx])
                backtrack(curr, idx + 1)
                curr[-1].pop()

            # Current character is part of a new substring
            curr.append([s[idx]])
            backtrack(curr, idx + 1)
            curr.pop()
        
        backtrack([], 0)
        return ans

        
"""
Valid substring = palindrome
Len 1 is always palindrome

At each character, we can either add it to the current substring
or end the current substring and the current character is the beginning
of a new substring

At every step, we check if all substring is a palindrome

For efficiency, a substring should be in the form of a list of chars
"""