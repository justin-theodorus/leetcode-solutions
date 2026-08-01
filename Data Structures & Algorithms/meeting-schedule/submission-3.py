"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        def overlap(intervalA, intervalB):
            return intervalA.start < intervalB.end and intervalB.start < intervalA.end
        
        intervals.sort(key = lambda x: x.start)
        curInterval = intervals[0]
        for i in range(1, len(intervals)):
            if overlap(curInterval, intervals[i]):
                return False
            curInterval = intervals[i]
        return True