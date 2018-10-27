#encoding:utf8
__author__ = 'gold'

'''
451.
Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        charList = []
        charDict = {}

        for char in s:
            if char not in charDict:
                charDict[char] = 0
            charDict[char] += 1

        while charDict:
            smallCount = 0
            smallKey = None
            for key in charDict:
                if charDict[key] > smallCount:
                    smallKey = key
                    smallCount = charDict[key]
            temp = [smallKey] * smallCount
            charList.append(''.join(temp))
            charDict.pop(smallKey)

        return ''.join(charList)

if __name__ == '__main__':
    print(Solution().frequencySort("tree"))