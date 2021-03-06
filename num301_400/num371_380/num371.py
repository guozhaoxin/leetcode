#encoding:utf8
__author__ = 'gold'

'''
 Sum of Two Integers
 
 Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        xor = a ^ b
        an = (a & b) << 1
        return self.getSum(xor,an)


if __name__ == '__main__':
    print(Solution().getSum(1,-1))