#encoding:utf8
__author__ = 'gold'

'''
Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        results = []

        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            a,b = b,a #保证a总是长度更长的

        index = 0
        carry = 0
        digitDic = {'0':0,'1':1}
        while index < len(a) and index < len(b):
            tempSum = digitDic[a[index]] + digitDic[b[index]] + carry
            if tempSum < 2:
                carry = 0
                results.append(str(tempSum))
            else:
                carry = 1
                results.append(str(tempSum - 2))
            index += 1

        if index < len(a):
            while index < len(a):
                tempSum = digitDic[a[index]] + carry
                if tempSum < 2:
                    carry = 0
                    results.append(str(tempSum))
                else:
                    carry = 1
                    results.append(str(0))
                index += 1
            if carry != 0:
                results.append(str(1))
        else:
            if carry != 0:
                results.append(str(1))

        return ''.join(results)[::-1]

if __name__ == '__main__':
    a = '11'
    b = '1'

    a = "1010"
    b = "1011"

    # a = '1111'
    # b = '1111'

    print(Solution().addBinary(a,b))