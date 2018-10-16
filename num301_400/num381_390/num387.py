#encoding:utf8
__author__ = 'gold'

'''
387.
First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charDic = {}
        for char in s:
            if char not in charDic:
                charDic[char] = 0
            charDic[char] += 1

        for index in range(len(s)):
            if charDic[s[index]] == 1:
                return index

        return -1

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet1 = set()
        charSet2 = set()
        for char in s:
            if char not in charSet2:
                if char not in charSet1:
                    charSet1.add(char)
                else:
                    charSet2.add(char)
                    charSet1.remove(char)

        if not charSet1:
            return -1
        for i in range(len(s)):
            if s[i] in charSet1:
                return i

if __name__ == '__main__':
    print(Solution().firstUniqChar('abcda'))