# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        res = []
        if len(intervals) <= 1:
            return intervals
        last_start = intervals[0].start
        last_end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start <= last_end:
                if last_end < intervals[i].end:
                    last_end = intervals[i].end
            else:
                res.append(Interval(last_start, last_end))
                last_start = intervals[i].start
                last_end = intervals[i].end
        res.append(Interval(last_start, last_end))
        return res
