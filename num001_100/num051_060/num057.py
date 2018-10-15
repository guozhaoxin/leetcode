#encoding:utf8
__author__ = 'gold'

'''
Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        results = []

        if not intervals:
            results.append(newInterval)
            return results

        if newInterval.end < intervals[0].start:
            results.append(newInterval)
            results.extend(intervals)
            return results

        if newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals

        temp = []
        index = 0
        while index < len(intervals):
            if intervals[index].start < newInterval.start:
                temp.append(intervals[index])
                index += 1
            else:
                break

        if index == len(intervals):
            temp.append(newInterval)
        else:
            temp.append(newInterval)
            while index < len(intervals):
                temp.append(intervals[index])
                index += 1

        results.append(temp[0])  # 先构建第一个元素

        index = 1
        while index < len(temp):
            if temp[index].start < results[-1].end:
                if temp[index].end < results[-1].end:
                    pass
                else:
                    results[-1].end = temp[index].end
                index += 1
            elif temp[index].start == results[-1].end:
                results[-1].end = temp[index].end
                index += 1
            else:
                results.append(temp[index])
                index += 1

        return results

def p(intervals):
    for interval in intervals:
        print(interval.start,interval.end)

if __name__ == '__main__':
    intervals = []
    # intervals.append(Interval(1,3))
    # intervals.append(Interval(6,9))

    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
    intervals.append(Interval(1,2))
    intervals.append(Interval(3,5))
    intervals.append(Interval(6,7))
    intervals.append(Interval(8,10))
    intervals.append(Interval(12,16))

    results = Solution().insert(intervals,Interval(4,8))
    p(results)