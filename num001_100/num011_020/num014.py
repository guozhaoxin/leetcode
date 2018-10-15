#encoding:utf8
__author__ = 'gold'

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        strs.sort(key=len)

        print(strs)
        index = len(strs[0])
        while index >=0:
            for s in strs:
                if not s.startswith(strs[0][0:index]):
                    index -= 1
                    break
            else:
                return strs[0][0:index]
        return ''



if __name__ == '__main__':
    s = ['a','ab','abc','ab']
    print(Solution().longestCommonPrefix(s))