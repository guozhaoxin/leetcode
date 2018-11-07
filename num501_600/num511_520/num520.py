#encoding:utf8
__author__ = 'gold'

'''
520.
Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True

        if len(word) == 2:
            if word[0] >= 'a' and word[1] <= 'Z':
                return False
            return True

        if word[0] >= 'a':
            pre = 1
        else:
            pre = 0

        for index in range(len(word)):

            if word[index] >= 'a':
                cur = 1
            else:
                cur = 0
            if pre == cur:
                continue
            else:
                if pre == 1:
                    return False
                if index == 1:
                    pre = cur
                    continue
                return False
        return True

if __name__ == '__main__':
    print(Solution().detectCapitalUse('USA'))
    print(Solution().detectCapitalUse('Flag'))
    print(Solution().detectCapitalUse('FlaG'))