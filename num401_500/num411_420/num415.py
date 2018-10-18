#encoding:utf8
__author__ = 'gold'

'''
415.
Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        char2num = {
            '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9
        }
        num2char = {
            0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'
        }
        results = []
        remainder = 0
        while index2 >= 0 and index1 >= 0:
            curSum = char2num[num1[index1]] + char2num[num2[index2]] + remainder
            results.append(num2char[curSum % 10])
            remainder = curSum // 10
            index1 -= 1
            index2 -= 1
        while index1 >= 0:
            curSum = char2num[num1[index1]] + remainder
            results.append(num2char[curSum % 10])
            remainder = curSum // 10
            index1 -= 1
        while index2 >= 0:
            curSum = char2num[num2[index2]] + remainder
            results.append(num2char[curSum % 10])
            remainder = curSum // 10
            index2 -= 1
        if remainder != 0:
            results.append(num2char[remainder])

        return ''.join(results[::-1])

if __name__ == '__main__':
    print(Solution().addStrings('828','856'))