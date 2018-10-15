#encoding:utf8
__author__ = 'gold'

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True

        braList = []
        leftBraDic = {'{':'}','[':']','(':')'}
        rightBraDic = {'}':'{',']':'[',')':'('}
        for char in s:
            if char in leftBraDic:
                braList.append(char)
            else:
                if len(braList) == 0:
                    return False
                elif braList[-1] == rightBraDic[char]:
                    del braList[-1]
                else:
                    return False
        if len(braList) == 0:
            return True
        return False

if __name__ == '__main__':
    print(Solution().isValid('()'))
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('(]'))
    print(Solution().isValid('([)]'))