class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        prevRow = []
        m = len(text1)
        n = len(text2)

        # build first Row
        for j in range(n):
            if j == 0:
                if text1[0] == text2[0]:
                    prevRow.append(1)
                else:
                    prevRow.append(0)
            else:
                if text1[0] == text2[j]:
                    prevRow.append(1)
                else:
                    prevRow.append(prevRow[-1])
        
        # build the rest of the rows
        curRow = []
        for i in range(1, m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if j == 0:
                        curRow.append(1)
                    else:
                        curRow.append(prevRow[j - 1] + 1)
                else:
                    if j == 0:
                        curRow.append(prevRow[0])
                    else:
                        curRow.append(max(prevRow[j], curRow[j - 1]))
                    
            prevRow = curRow
            curRow = []
        
        return prevRow[-1]