class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        answer = {}

        sortedIntervals = sorted(intervals, key = lambda x: x[1] - x[0] + 1)

        for interval in sortedIntervals:
            for i in range(interval[0], interval[1] + 1):
                if i not in answer:
                    answer[i] = interval[1] - interval[0] + 1
                
        
        res = []
        for query in queries:
            if query not in answer:
                res.append(-1)
            else:
                res.append(answer[query])
        return res