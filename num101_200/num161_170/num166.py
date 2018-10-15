#encoding:utf8
__author__ = 'gold'

'''
Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        sign = ''
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0 :
            sign = '-'
            if numerator < 0 :
                numerator = -numerator
            else:
                denominator = -denominator
        q,r = divmod(numerator,denominator)
        if r == 0:
            return sign + str(q)

        intStr = str(q) + '.'
        remainder = numerator % denominator * 10 #获得余数部分
        temp = ''
        numDict = {}
        l = 0
        while True:
            if remainder in numDict:
                temp = temp[0:numDict[remainder]] + '(' + temp[numDict[remainder]:] + ')'
                break
            q,r = divmod(remainder,denominator)
            if r == 0:
                temp += str(q)
                break
            elif remainder < denominator:
                temp += '0'
                numDict[remainder] = l
                remainder *= 10
            else:
                temp += str(q)
                numDict[remainder] = l
                remainder = r * 10

            l += 1
        return sign + intStr + temp

if __name__ == '__main__':
    # print(Solution().fractionToDecimal(1,2))
    # print(Solution().fractionToDecimal(2,3))
    # print(Solution().fractionToDecimal(4,7))
    # print(Solution().fractionToDecimal(6,7))
    # print(Solution().fractionToDecimal(5,9))
    # print(Solution().fractionToDecimal(9,17))
    # print(Solution().fractionToDecimal(100,123),100/123)
    # print(Solution().fractionToDecimal(15,36),15/36)
    # print(Solution().fractionToDecimal(4,333),4/333)
    # print(Solution().fractionToDecimal(-50,8),-50/8)
    print(Solution().fractionToDecimal(-40,11),40/-11)