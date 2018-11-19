#encoding:utf8
__author__ = 'gold'

'''
678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
'''


class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = high = 0

        for index in range(len(s)):
            if s[index] == '(':
                low += 1
                high += 1
            elif s[index] == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False

        return low == 0


if __name__ == '__main__':
    print(Solution().checkValidString("()"))
    print(Solution().checkValidString("(*)"))
    print(Solution().checkValidString("(*))"))
    print(Solution().checkValidString("("))
    print(Solution().checkValidString("*"))
    print(Solution().checkValidString(")"))
    print(Solution().checkValidString("*)"))
    print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
