#encoding:utf8
__author__ = 'gold'

'''
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #处理特殊情况
        if len(s) < 2:
            return s

        middleIndex = 0 #标记中间那个索引，但是要考虑奇偶性
        maxLengthen = 0 #标记最长字符串的长度
        leftIndex = 0 #标记最长字符串的左边索引
        rightIndex = 0 #标记最长字符串的右边索引

        while middleIndex < len(s):
            #先处理奇数的情况
            left = middleIndex - 1
            right = middleIndex + 1
            while left >= 0 and right < len(s) and (s[left] == s[right]):
                left -= 1
                right += 1
            currL = right - left - 1
            if maxLengthen < currL:
                maxLengthen = currL
                leftIndex = left + 1
                rightIndex = right - 1

            #处理偶数的情况
            left = middleIndex
            right = middleIndex + 1
            while left >= 0 and right < len(s) and (s[left] == s[right]):
                left -= 1
                right += 1
            currL = right - left - 1
            if maxLengthen < currL:
                maxLengthen = currL
                leftIndex = left + 1
                rightIndex = right - 1
            middleIndex += 1
        return s[leftIndex:rightIndex + 1]


if __name__ == '__main__':
    s = 'bbb'
    print(Solution().longestPalindrome(s))