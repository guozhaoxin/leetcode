#encoding:utf8
__author__ = 'gold'

'''
Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sDic = {}
        tDic = {}
        for char in s:
            if char not in sDic:
                sDic[char] = 0
            sDic[char] += 1
        for char in t:
            if char not in tDic:
                tDic[char] = 0
            tDic[char] += 1

        for char in sDic:
            if char not in tDic or sDic[char] != tDic[char]:
                return False

        for char in tDic:
            if char not in sDic or tDic[char] != sDic[char]:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isAnagram(s = "anagram", t = "nagaram"))
    print(Solution().isAnagram(s = "rat", t = "car"))