class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)

        res = []
        window = set()

        l = 0
        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
            counter[s[r]] -= 1
            if counter[s[r]] == 0:
                window.remove(s[r])
            
            if len(window) == 0:
                res.append(r - l + 1)
                l = r + 1
        return res


"""
Append everytime a count reaches 0
"""