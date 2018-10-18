#encoding:utf8
__author__ = 'gold'

'''
97.
Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dfs(s1,s2,s3,0,0,0)


    def dfs(self,s1,s2,s3,index1,index2,index3):
        if index3 == len(s3):
            return True
        if index1 == len(s1):
            return s2[index2:] == s3[index3:]
        if index2 == len(s2):
            return s1[index1:] == s3[index3:]
        if s1[index1] != s3[index3] and s2[index2] != s3[index3]:
            return False
        tempIndex1 = index1
        tempIndex2 = index2
        while tempIndex1 < len(s1) and tempIndex2 < len(s2) and index3 < len(s3):
            if s3[index3] != s1[tempIndex1] or s3[index3] != s2[tempIndex2]:
                break
            tempIndex1 += 1
            tempIndex2 += 1
            index3 += 1
        if index3 == len(s3):
            return True
        if tempIndex1 == len(s1):
            return s2[tempIndex2:] == s3[index3:]
        if tempIndex2 == len(s2):
            return s1[tempIndex1:] == s3[index3:]
        if s1[tempIndex1] != s3[index3] and s2[tempIndex2] != s3[index3]:
            return False
        if s1[tempIndex1] == s3[index3]:
            tempIndex1 += 1
            index1 = tempIndex1

        if s2[tempIndex2] == s3[index3]:
            tempIndex2 += 1
            index2 = tempIndex2

        index3 += 1

        return self.dfs(s1,s2,s3,index1,index2,index3)

if __name__ == '__main__':
    print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
    print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print(Solution().isInterleave(s1,s2,s3))
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print(Solution().isInterleave(s1,s2,s3))
    print(Solution().isInterleave('aa','ab','aaba'))