class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def overlap(intervalA, intervalB):
            return intervalA[0] < intervalB[1] and intervalB[0] < intervalA[1]
        intervals.sort()
        curInterval = intervals[0]
        res = 0

        for i in range(1, len(intervals)):
            if overlap(curInterval, intervals[i]):
                res += 1
                if intervals[i][1] < curInterval[1]:
                    # keep the interval that ends earlier
                    curInterval = intervals[i]
            else:
                curInterval = intervals[i]
        
        return res



"""
[[1,2], [1,3], [4,7]]
"""