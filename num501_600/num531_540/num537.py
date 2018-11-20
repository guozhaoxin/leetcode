#encoding:utf8
__author__ = 'gold'

'''
537. Complex Number Multiplication
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

'''


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        AB = a.split('+')
        A = int(AB[0])
        B = int(AB[1][:-1])
        CD = b.split('+')
        C = int(CD[0])
        D = int(CD[1][:-1])
        shiPart = A * C - B * D
        xuPart = B * C + A * D
        return str(shiPart) + '+' + str(xuPart) + 'i'


if __name__ == '__main__':
    print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))