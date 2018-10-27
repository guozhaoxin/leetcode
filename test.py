#encoding:utf8
__author__ = 'gold'

b = ['1df','bx','cy']

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        ["flower","flow","flight"]
        """
        if not strs:
            return ""

        for x in zip(*strs):
            print(x)

        print('****')

        for x,y in enumerate(zip(*strs)):
            print(x,y)

        for i,ch in enumerate(zip(*strs)):
            if len(set(ch)) != 1:
                return strs[0][:i]
        else:
            return min(strs,key = len)

print(chr(711100))