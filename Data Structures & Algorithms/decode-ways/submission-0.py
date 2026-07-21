class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # take one digit, depends on the number of ways to decode from s[i+1:]
                dp[i] = dp[i + 1]
            
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                # take two digit, depends on the number of way to decode from s[i+2:]
                dp[i] += dp[i + 2]
        return dp[0]


"""
How many ways to decode s[i:]

0 if s[i] == "0"
Can either be 1 digit or 2 digit
"""