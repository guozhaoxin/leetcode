#encoding:utf8
__author__ = 'gold'

'''
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

'''

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        assert len(s) == len(t)
        char2numDic = {}
        num2charDic = {}

        for index in range(len(s)):
            s_char = s[index]
            t_char = t[index]
            num = ord(t_char)

            if s_char in char2numDic:
                if char2numDic[s_char] != num:
                    return False
            if num in num2charDic:
                if num2charDic[num] != s_char:
                    return False

            char2numDic[s_char] = num
            num2charDic[num] = s_char


        return True

if __name__ == '__main__':
    print(Solution().isIsomorphic('egg','add'))
    print(Solution().isIsomorphic('foo','bar'))
    print(Solution().isIsomorphic('paper','title'))