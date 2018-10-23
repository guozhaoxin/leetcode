#encoding:utf8
__author__ = 'gold'

'''
507.
Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        endFlag = num ** .5
        sum = 1

        divisor = 2
        while divisor <= endFlag:
            if num % divisor == 0:
                quotient = num // divisor
                if quotient != divisor:
                    sum += quotient + num // quotient
                else:
                    sum += divisor + quotient
            divisor += 1

        return sum == num

if __name__ == '__main__':
    print(Solution().checkPerfectNumber(28))
    print(Solution().checkPerfectNumber(6))
    print(Solution().checkPerfectNumber(4))
    print(Solution().checkPerfectNumber(25))