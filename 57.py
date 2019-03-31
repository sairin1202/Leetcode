# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        intervals = sorted(intervals, key = lambda x: x.start)
        res = []
        start = -1
        end = -1
        #find end
        for i in range(len(intervals)):
            if newInterval.end < intervals[i].start:
                end = i
                break
        if end == -1:
            end = len(intervals)

        # find start
        for i in range(len(intervals)):
            if newInterval.start <= intervals[i].end:
                start = i
                break
        if start == -1:
            start = len(intervals)


        # print(start, end)
        if start == len(intervals):
            intervals.append(newInterval)
            return intervals
        if start == 0 and end == 0:
            intervals.insert(0, newInterval)
            return intervals


        i_start = intervals[start].start if intervals[start].start < newInterval.start else newInterval.start
        i_end = intervals[end-1].end if intervals[end-1].end > newInterval.end else newInterval.end
        # print(i_start, i_end)
        for _ in range(end-start):
            intervals.pop(start)
        intervals.insert(start, Interval(i_start, i_end))
        return intervals


        
