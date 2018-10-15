#encoding:utf8
__author__ = 'gold'

'''
Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s
        if len(s) == 1:
            return s
        vowSet = set('aeiouAEIOU')
        leftStr = ''
        rightStr = ''
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right:
                if s[left] in vowSet:
                    break
                leftStr += s[left]
                left += 1
            while right > left:
                if s[right] in vowSet:
                    break
                rightStr += s[right]
                right -= 1
            if left == right:
                leftStr += s[left]
            else:
                leftStr += s[right]
                rightStr += s[left]
            left += 1
            right -= 1
        if left == right:
            leftStr += s[left]

        return leftStr + rightStr[::-1]

class Solution1:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        strList = []
        vowSet = set('aeiouAEIOU')
        for index in range(len(s)):
            if s[index] in vowSet:
                stack.append(s[index])
                strList.append('*')
            else:
                strList.append(s[index])
        for index in range(len(s)):
            if strList[index] == '*':
                strList[index] = stack.pop()

        return ''.join(strList)
if __name__ == '__main__':
    print(Solution().reverseVowels('hello'))
    print(Solution1().reverseVowels('hello'))
    print(Solution().reverseVowels('leetcode'))
    print(Solution1().reverseVowels('leetcode'))
    print(Solution().reverseVowels('a a'))
    print(Solution1().reverseVowels('a a'))