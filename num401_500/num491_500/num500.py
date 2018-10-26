#encoding:utf8
__author__ = 'gold'

'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keySetLine1 = set('qwertyuiopQWERTYUIOP')
        keySetLine2 = set('asdfghjklASDFGHJKL')
        keySetLine3 = set('zxcvbnmZXCVBNM')

        results = []

        for word in words:
            if word[0] in keySetLine1:
                line = keySetLine1
            elif word[0] in keySetLine2:
                line = keySetLine2
            else:
                line = keySetLine3
            for i in range(1,len(word)):
                if word[i] not in line:
                    break
            else:
                results.append(word)

        return results

if __name__ == '__main__':
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))