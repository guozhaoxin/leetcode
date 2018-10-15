#encoding:utf8
__author__ = 'gold'

'''
Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        if not s:
            return sum
        for char in s:
            sum = sum * 26 + (ord(char) - 64)

        return sum

if __name__ == '__main__':
    print(Solution().titleToNumber('A'))
    print(Solution().titleToNumber('AB'))
    print(Solution().titleToNumber('ZY'))