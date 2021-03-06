#encoding:utf8
__author__ = 'gold'

'''
326.
Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

if __name__ == '__main__':
    print(Solution().isPowerOfThree(3))
    print(Solution().isPowerOfThree(6))
    print(Solution().isPowerOfThree(9))
    print(Solution().isPowerOfThree(13))
    print(Solution().isPowerOfThree(27))