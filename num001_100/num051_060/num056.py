#encoding:utf8
__author__ = 'gold'

'''
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        results = []
        if not intervals:
            return results

        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x.start) #先给它排序再说

        results.append(Interval(intervals[0].start,intervals[0].end)) #先构建第一个元素

        index = 1
        while index < len(intervals):
            if intervals[index].start < results[-1].end:
                if intervals[index].end < results[-1].end:
                    pass
                else:
                    results[-1].end = intervals[index].end
                index += 1
            elif intervals[index].start == results[-1].end:
                results[-1].end = intervals[index].end
                index += 1
            else:
                results.append(intervals[index])
                index += 1

        return results

if __name__ == '__main__':
    intervals = []
    intervals.append(Interval(1,3))
    intervals.append(Interval(2,6))
    intervals.append(Interval(8,10))
    intervals.append(Interval(15,18))
    intervals.append(Interval(1,4))
    intervals.append(Interval(4,5))
    # intervals.append(Interval(3,100))
    # intervals.append(Interval(2,200))
    # intervals.append(Interval(1,300))
    results = Solution().merge(intervals)
    for s in results:
        print(s.start,s.end)