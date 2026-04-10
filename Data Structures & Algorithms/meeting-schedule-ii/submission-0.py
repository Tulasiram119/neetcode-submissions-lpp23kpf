"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # I think it involves sorting and finding the non over lapping meetings
        # We need to find number of over laping.
        # (0,40),(5,10),(15,20)
        # As you see here 0 to 40 is in one room, 5,10 in one room once that 
        # completed 15,20 in another room
        # 
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,interval.end)
        return len(min_heap)
        