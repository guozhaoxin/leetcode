#encoding:utf8
__author__ = 'gold'

'''
539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''


class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timeList = []
        for time in timePoints:
            time_split = time.split(':')
            time_minute = int(time_split[0]) * 60 + int(time_split[1])
            timeList.append(time_minute)

        timeList.sort()
        timeList.append(1440 + timeList[0])
        difference = 24 * 60
        for index in range(len(timeList) - 1):
            difference = min(difference,timeList[index + 1] - timeList[index])
            if difference == 0:
                break
        return difference

if __name__ == '__main__':
    print(Solution().findMinDifference(["23:59","00:00"]))
    print(Solution().findMinDifference(["05:31","22:08","00:35"]))