#encoding:utf8
__author__ = 'gold'

'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1 #标记原始数据是否为正数
        sum = 0
        x = abs(x)
        while x != 0:
            sum *= 10
            sum += x % 10
            x = int(x / 10)
        sum *= flag
        if sum > 2147483647 or sum < -2147483648:
            return 0
        return sum


if __name__ == '__main__':
    print(Solution().reverse(-1243))
    print(Solution().reverse(-11111111111111111111111111111111))
    print(Solution().reverse(-0))
