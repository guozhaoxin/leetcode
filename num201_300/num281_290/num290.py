#encoding:utf8
__author__ = 'gold'

'''
290.
Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordsList = str.split(' ')
        if len(pattern) != len(wordsList):
            return False
        p2sMapDic = {}
        s2pMapDic = {}
        for i,char in enumerate(pattern):
            if char not in p2sMapDic and wordsList[i] not in s2pMapDic:
                p2sMapDic[char] = wordsList[i]
                s2pMapDic[wordsList[i]] = char
            elif char in p2sMapDic and wordsList[i] in s2pMapDic:
                if char == s2pMapDic[wordsList[i]] and p2sMapDic[char] == wordsList[i]:
                    continue
                else:
                    return False
            else:
                return False

        return True


if __name__ == '__main__':
    print(Solution().wordPattern('abba','dog cat cat fish'))
    print(Solution().wordPattern('abba','dog cat cat dog'))