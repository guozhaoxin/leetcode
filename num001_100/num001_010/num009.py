#encoding:utf8
__author__ = 'gold'

'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x < 10:
            return True
        if x < 0:
            return False
        if x % 10 == 0:
            return False

        sum = 0
        previous = x
        while x:
            if x == sum:
                return True
            elif x > sum:
                sum = sum * 10 + x % 10
                previous = x
                x //= 10
            else:
                if previous == sum:
                    return True
                else:
                    return False
        print(x,previous,sum)
        return False

if __name__ == '__main__':
    # print(Solution().isPalindrome(123))
    # print(Solution().isPalindrome(123321))
    # print(Solution().isPalindrome(12321))
    # print(Solution().isPalindrome(+123))
    # print(Solution().isPalindrome(+123321))
    # print(Solution().isPalindrome(-123))
    # print(Solution().isPalindrome(10))
    # print(Solution().isPalindrome(0))
    print(Solution().isPalindrome(1))


