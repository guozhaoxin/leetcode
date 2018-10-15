#encoding:utf8
__author__ = 'gold'

'''
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            while left <= right:
                if not s[left].isalnum():
                    left += 1
                else:
                    break
            if left > right:
                return True

            while right >= left:
                if not s[right].isalnum():
                    right -= 1
                else:
                    break
            if right < left:
                return True

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome("0P"))