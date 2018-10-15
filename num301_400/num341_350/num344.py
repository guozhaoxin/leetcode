#encoding:utf8
__author__ = 'gold'

'''
Reverse String

Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        result = ''
        index = len(s) - 1
        while index >= 0:
            result += s[index]
            index -= 1
        return result

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == '__main__':
    print(Solution().reverseString('ab c.d,ef g'))