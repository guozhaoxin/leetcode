#encoding:utf8
__author__ = 'gold'

'''
Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 1:
            return True

        left = 1
        right = num // 2
        while left <= right:
            mid = (left + right) // 2
            product = mid * mid
            if product == num:
                return True
            if product > num:
                right = mid - 1
            else:
                left += 1

        if right * right != num:
            return False
        return True

if __name__ == '__main__':
    print(Solution().isPerfectSquare(12))
    print(Solution().isPerfectSquare(16))
    print(Solution().isPerfectSquare(4))