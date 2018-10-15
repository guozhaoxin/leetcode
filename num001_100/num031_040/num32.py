#encoding:utf8
__author__ = 'gold'

'''
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        longest = start_idx = 0
        for idx in range(len(s)):
            if s[idx] == ")":
                if stk:
                    stk.pop()
                    longest = max(longest, idx - stk[-1] if stk else idx - start_idx + 1)
                else:
                    start_idx = idx + 1
                    stk = []
            else:
                stk.append(idx)
        return longest

if __name__ == '__main__':
    s = ")()())"
    s = "(())"
    s = '()'
    s = "()(()"
    s = '()())()()()(()'
    s = ''
    # s = '(()'
    # s = "(()(((()"
    # s = '(()()'
    print(Solution().longestValidParentheses(s))