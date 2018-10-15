#encoding:utf8
__author__ = 'gold'

'''
Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

from common.calculate import factorial

def getTailZeroCou(num):
    count = 0
    while num % 10 == 0:
        count += 1
        num = num // 10
    return count


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 0

        num_zeros = 0
        pow_of_5 = 5

        while pow_of_5 <= n:
            num_zeros += n // pow_of_5
            pow_of_5 *= 5

        return num_zeros



if __name__ == '__main__':
    print(Solution().trailingZeroes(1808548329))
    # for i in range(1000):
    #     num = factorial(i)
    #     a = getTailZeroCou(num)
    #     b = Solution().trailingZeroes(i)
    #     print(i,a,b)

        # if a != b:
        #     print(i,a,b)