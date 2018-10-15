#encoding:utf8
__author__ = 'gold'

'''
Reverse Words in a String
 
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        startIndex = 0
        wordStack = []

        while startIndex < len(s):
            while startIndex < len(s) and s[startIndex] == ' ':
                startIndex += 1
            if startIndex == len(s):
                break

            endIndex = startIndex
            while endIndex < len(s) and s[endIndex] != ' ':
                endIndex += 1
            wordStack.append(s[startIndex:endIndex])
            startIndex = endIndex + 1

        wordStack.reverse()
        return ' '.join(wordStack)

if __name__ == '__main__':
    print(Solution().reverseWords("the sky is blue"))