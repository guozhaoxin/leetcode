#encoding:utf8
__author__ = 'gold'

'''
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 10:
            return num

        numStrList = list(str(num))
        index = 1
        while index < len(numStrList):
            if numStrList[index - 1] < numStrList[index]:
                break
            index += 1
        if index == len(numStrList):
            return num

        maxBitIindex = index
        while index < len(numStrList):
            if numStrList[index] >= numStrList[maxBitIindex]:
                maxBitIindex = index
            index += 1

        index = 0
        while index < len(numStrList):
            if numStrList[index] < numStrList[maxBitIindex]:
                numStrList[index],numStrList[maxBitIindex] = numStrList[maxBitIindex],numStrList[index]
                return int(''.join(numStrList))
            index += 1


        return int(''.join(numStrList))

if __name__ == '__main__':
    print(Solution().maximumSwap(2736))
    print(Solution().maximumSwap(9973))
    print(Solution().maximumSwap(9678))
    print(Solution().maximumSwap(115))
    print(Solution().maximumSwap(1993))
    print(Solution().maximumSwap(10909091))
    print(Solution().maximumSwap(98368))