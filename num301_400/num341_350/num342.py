#encoding:utf8
__author__ = 'gold'

'''
Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 4 != 0:
            return False

        while num:
            if num % 4 != 0:
                return False
            num = num // 4
            if num == 1:
                return True
        return True

if __name__ == '__main__':
    print(Solution().isPowerOfFour(16))
    print(Solution().isPowerOfFour(4))
    print(Solution().isPowerOfFour(2))
    print(Solution().isPowerOfFour(123))
    print(Solution().isPowerOfFour(1234))
    print(Solution().isPowerOfFour(1024))
    print(Solution().isPowerOfFour(65536))
    print(Solution().isPowerOfFour(20))