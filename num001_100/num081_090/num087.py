#encoding:utf8
__author__ = 'gold'

'''
87.
Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
'''


class Solution:
    def isScramble(self, s1:str, s2:str):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 is None and s2 is not None:
            return False
        if s2 is None and s1 is not None:
            return False
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1Dic = {}
        s2Dic = {}
        for i in range(len(s1)):
            if s1[i] not in s1Dic:
                s1Dic[s1[i]] = 0
            s1Dic[s1[i]] += 1
            if s2[i] not in s2Dic:
                s2Dic[s2[i]] = 0
            s2Dic[s2[i]] += 1
        for key in s1Dic:
            if key not in s2Dic or s1Dic[key] != s2Dic[key]:
                return False

        for i in range(1,len(s1)):
            result = self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])
            if result:return True
            result = self.isScramble(s1[:i],s2[len(s1) - i:]) and self.isScramble(s1[i:],s2[:len(s1) - i])
            if result:return True

        return False

if __name__ == '__main__':
    # print(Solution().isScramble('great','rgtae'))
    print(Solution().isScramble('abc','bca'))