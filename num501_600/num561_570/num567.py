#encoding:utf8
__author__ = 'gold'

'''
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

from collections import defaultdict,Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Count = Counter(s1)
        leftIndex = 0
        end = len(s2) - len(s1) + 1
        while leftIndex < end:
            if s2[leftIndex] not in s1Count:
                leftIndex += 1
                continue

            s2Dic = {}
            rightIndex = leftIndex
            while rightIndex < len(s2):
                if s2[rightIndex] not in s1Count:
                    leftIndex = rightIndex + 1
                    break
                if s2[rightIndex] not in s2Dic:
                    s2Dic[s2[rightIndex]] = 0
                s2Dic[s2[rightIndex]] += 1
                if s2Dic[s2[rightIndex]] > s1Count[s2[rightIndex]]:
                    while leftIndex < rightIndex and s1Count[s2[rightIndex]] < s2Dic[s2[rightIndex]]:
                        s2Dic[s2[leftIndex]] -= 1
                        if s2Dic[s2[leftIndex]] == 0:
                            s2Dic.pop(s2[leftIndex])
                        leftIndex += 1
                    # rightIndex += 1
                elif rightIndex - leftIndex + 1 == len(s1):
                    return True
                rightIndex += 1


        return False

if __name__ == '__main__':
    print(Solution().checkInclusion('ab','bad'))
    print(Solution().checkInclusion('ab',"eidboaoo"))
    print(Solution().checkInclusion('a',"ab"))
    print(Solution().checkInclusion('adc',"dcda"))