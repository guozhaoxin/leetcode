#encoding:utf8
__author__ = 'gold'

'''
Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        index = len(s) - 1
        while index >= 0:
            if s[index] == ' ':
                index -= 1
            else:
                break
        if index == -1:
            return 0

        lengthen = 0
        while index >= 0:
            if s[index] != ' ':
                lengthen += 1
                index -= 1
            else:
                break
        return lengthen

if __name__ == '__main__':
    print(Solution().lengthOfLastWord('abcd'))