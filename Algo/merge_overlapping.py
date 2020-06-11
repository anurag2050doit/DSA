"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

REF: https://www.interviewbit.com/problems/merge-overlapping-intervals/

"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, I):
        res = []
        I.sort(key=lambda i: i.start)
        for i in I:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res


if __name__ == '__main__':
    obj = Solution()
    q1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    inters = [Interval(s=x[0], e=x[1]) for x in q1]
    new_inters = obj.merge(inters)
    print([(x.start, x.end) for x in new_inters])
    q2 = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6)]
    inters = [Interval(s=x[0], e=x[1]) for x in q2]
    new_inters = obj.merge(inters)
    print([(x.start, x.end) for x in new_inters])
