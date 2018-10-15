#encoding:utf8
__author__ = 'gold'

'''
Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0:
            return 0

        if m == n:
            return m

        if n - m == 1:
            return m & n

        count = n - m + 1
        p = 1
        resultList = ['0' for i in range(32)]
        for i in range(32):
            temp = p & m
            if temp == 0:
                p = p << 1
                continue
            if count + m % p <= p:
                resultList[31 - i] = '1'
            p = p << 1
        return int(''.join(resultList),base=2)

if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(5,8))
    print(Solution().rangeBitwiseAnd(5,7))
    print(Solution().rangeBitwiseAnd(4,7))
    print(Solution().rangeBitwiseAnd(5,6))
    print(Solution().rangeBitwiseAnd(12,14))