"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda s: s.start)

        stack = []

        for i in intervals:
            start, end = i.start, i.end
            print(start)
            print(end)

            while stack and stack[-1] > start:
                return False
            
            stack.append(end)
        
        return True
