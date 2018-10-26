#encoding:utf8
__author__ = 'gold'

'''
504.
Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return '0'
        sign = '' if num >= 0 else '-'
        if num < 0:
            num = -num

        remainderStack = []
        while num:
            remainderStack.append(str(num % 7))
            num = num // 7

        remainderStack.reverse()
        return sign + ''.join(remainderStack)

if __name__ == '__main__':
    print(Solution().convertToBase7(100))
    print(Solution().convertToBase7(-14))