#encoding:utf8
__author__ = 'gold'

'''
Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''


class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 0
        if n < 10:
            return 1
        bit = self.getBit(n) #得到数的位数

        count = 0
        count += 10 ** (bit - 1) // 10

        return count


    def getBit(self,n):
        if n == 0:
            return 1
        bit = 0
        while n:
            n = n // 10
            bit += 1
        return bit


if __name__ == '__main__':
    print(Solution().countDigitOne(100))