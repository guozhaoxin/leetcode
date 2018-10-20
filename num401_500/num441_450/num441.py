#encoding:utf8
__author__ = 'gold'

'''
441.
Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 1
        while True:
            coinCounts = (row + 1) * row // 2
            if coinCounts == n:
                return row
            if coinCounts > n:
                return row - 1
            row += 1

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        import math
        row = int((math.sqrt(8 * n + 1) - 1) // 2)
        return row

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        while n >= count:
            n -= count
            count += 1
        return count - 1

if __name__ == '__main__':
    print(Solution().arrangeCoins(5))
    print(Solution().arrangeCoins(8))
    print(Solution().arrangeCoins(1))
    print(Solution().arrangeCoins(1804289383))
