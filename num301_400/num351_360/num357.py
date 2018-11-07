#encoding:utf8
__author__ = 'gold'

'''
357.
Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        count = 0

        base = self.jiecheng(9)
        while n > 0:
            if n == 1:
                count += 10
            elif n > 10:
                pass
            else:
                start = 11 - n
                temp = 1
                while start <= 9:
                    temp *= start
                    start += 1
                count+= 9 * temp
            n -= 1

        return count

    def jiecheng(self,n):
        producer = 1
        k = 1
        while k <= n:
            producer *= k
            k += 1
        return producer


class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691]
        if n >= 11:
            return results[-1]
        return results[n]


if __name__ == '__main__':
    for i in range(10):
        print(i,Solution().countNumbersWithUniqueDigits(i))