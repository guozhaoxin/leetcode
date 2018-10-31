#encoding:utf8
__author__ = 'gold'

'''
435.
Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0: return 0
        intervals.sort(key=lambda x: x.start)

        count = 0
        prev_interval = intervals[0]
        for cur_interval in intervals[1:]:
            # Case 1: Don't overlap
            if cur_interval.start >= prev_interval.end:
                prev_interval = cur_interval
            # Case 2: Overlap
            else:
                count += 1
                if prev_interval.end > cur_interval.end:
                    prev_interval = cur_interval
        return count

if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([ [1,2], [1,2], [1,2] ]))
    print(Solution().eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))
    print(Solution().eraseOverlapIntervals([ [1,2], [2,3] ]))