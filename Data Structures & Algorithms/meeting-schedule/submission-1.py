"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        by_start = sorted(intervals, key = lambda x:x.start)
        i = 0 
        while i < len(intervals) - 1:
            curr_end = by_start[i].end
            next_start = by_start[i+1].start
            if next_start < curr_end:
                return False
            i += 1
        return True
            
