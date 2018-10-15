#encoding:utf8
__author__ = 'gold'

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        results = []
        for i in range(numRows):
            results.append('')

        index = 0 #表示字符串的索引
        while index < len(s):
            for i in range(numRows):
                if index >= len(s):
                    break
                results[i] += s[index]
                index += 1
            for i in range(numRows - 2,0,-1):
                if index >= len(s):
                    break
                results[i] += s[index]
                index += 1
            # index += 1
        out = ''
        for zazg in results:
            out += zazg
        return out

if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING',4))