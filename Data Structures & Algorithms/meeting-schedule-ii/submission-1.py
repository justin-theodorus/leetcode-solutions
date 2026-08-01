"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        def overlap(intervalA: Interval, intervalB: Interval) -> bool:
            return (intervalA.start < intervalB.end) and (intervalB.start < intervalA.end)
        intervals.sort(key = lambda x: x.start)
        meetingRooms = {}
        roomNo = 1

        for interval in intervals:
            inserted = False
            for i in range(1, roomNo):
                if not overlap(interval, meetingRooms[i]):
                    meetingRooms[i] = interval
                    inserted = True
                    break
                
            if not inserted:
                meetingRooms[roomNo] = interval
                roomNo += 1
        
        return roomNo - 1