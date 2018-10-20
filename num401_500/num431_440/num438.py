#encoding:utf8
__author__ = 'gold'

'''
438.
Find All Anuagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(p) > len(s):
            return result
        if len(p) == 1:
            for index in range(len(s)):
                if s[index] == p:
                    result.append(index)
            return result

        pDic = {}
        for char in p:
            if char not in pDic:
                pDic[char] = 0
            pDic[char] += 1

        startIndex = 0
        while startIndex <= len(s) - len(p):

            if s[startIndex] not in pDic:
                startIndex += 1
                continue

            sDic = {s[startIndex]:1}
            endIndex = startIndex + 1
            while startIndex <= len(s) - len(p) and endIndex < startIndex + len(p):
                if s[endIndex] not in pDic:
                    startIndex = endIndex + 1
                    endIndex = len(s)
                    break
                if s[endIndex] not in sDic:
                    sDic[s[endIndex]]= 0
                sDic[s[endIndex]] += 1
                if sDic[s[endIndex]] > pDic[s[endIndex]]:
                    while startIndex <= endIndex:
                        if s[startIndex] == s[endIndex]:
                            sDic[s[endIndex]] -= 1
                            startIndex += 1
                            break
                        sDic[s[startIndex]] -= 1
                        startIndex += 1
                if endIndex - startIndex + 1 == len(p):
                    result.append(startIndex)
                    sDic[s[startIndex]] -= 1
                    startIndex += 1
                endIndex += 1
        return result

if __name__ == '__main__':
    print(Solution().findAnagrams('abab','ab'))
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s,p))
    print(Solution().findAnagrams("acdcaeccde",'c'))