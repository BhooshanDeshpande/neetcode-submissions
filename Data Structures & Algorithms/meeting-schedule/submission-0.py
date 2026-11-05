"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
            Brute force : 
                sort all the interval list by start times (n log n)
                iterate until second to last : 
                    check if end(i) - start(i+1) <= 0 
                        if yes : False
                return true 

            Time complexity = o(n log n) + o(n) = o(n log n) 
        """

        sorted_intervals = sorted(intervals, key = lambda x: x.start)
        for index in range(0, len(sorted_intervals)-1):
            next_start = sorted_intervals[index+1].start
            current_start = sorted_intervals[index].start 
            current_end = sorted_intervals[index].end

            if current_start <= next_start and current_end > next_start:
                return False
            
        return True
