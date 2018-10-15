#encoding:utf8
__author__ = 'gold'

'''
Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        if x <= 3:
            return 1

        right = x // 2 #因为正常情况下，开方后的数据不会比一半大
        left = 2

        while left <= right:
            print(left,right)
            mid = (left + right) // 2
            temp = mid * mid

            if temp == x:
                return mid
            elif temp < x:
                left = mid + 1
            else:
                right = mid - 1
        return (left + right) // 2

if __name__ == '__main__':
    for i in range(1):
        print(i,Solution().mySqrt(i))

    print(Solution().mySqrt(435346565324))