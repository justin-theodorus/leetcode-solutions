class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(intervalA, intervalB):
            return intervalA[0] <= intervalB[1] and intervalB[0] <= intervalA[1]
        
        def mergeTwo(intervalA, intervalB):
            return [min(intervalA[0], intervalB[0]), max(intervalA[1], intervalB[1])]
        
        intervals.sort(key = lambda x: x[0])
        curInterval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if overlap(curInterval, intervals[i]):
                curInterval = mergeTwo(curInterval, intervals[i])
            else:
                res.append(curInterval)
                curInterval = intervals[i]
        
        res.append(curInterval)
        return res
