#encoding:utf8
__author__ = 'gold'

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #先处理特殊的两种情况
        if not s:
            return 0
        if len(s) == 1:
            return 1

        left = 0 #左边指针的索引
        right = 1 #右边指针的索引
        longestLen = 1 #最长子序列长度
        alpDict = {s[0]:0,} #标记出现的所有字母，键为字母，值为索引

        while right < len(s):
            if s[right] in alpDict and alpDict[s[right]] >= left:
                longestLen = max(longestLen,right - left)
                left = alpDict[s[right]] + 1
            # else:
            #     alpDict[s[right]] = right
            alpDict[s[right]] = right
            right += 1
        return max(longestLen,right - left)

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))
    print(Solution().lengthOfLongestSubstring('bbbb'))
