#encoding:utf8
__author__ = 'gold'

'''
389.
Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dic = {}
        t_dic = {}
        index = 0
        while index < len(s):
            if s[index] not in s_dic:
                s_dic[s[index]] = 0
            s_dic[s[index]] += 1
            if t[index] not in t_dic:
                t_dic[t[index]] = 0
            t_dic[t[index]] += 1
            index += 1
        if t[index] not in t_dic:
            t_dic[t[index]] = 0
        t_dic[t[index]] += 1

        for key in t_dic:
            if key not in s_dic:
                return key
            if t_dic[key] != s_dic[key]:
                return key

if __name__ == '__main__':
    print(Solution().findTheDifference('abcd','abcde'))