#encoding:utf8
__author__ = 'gold'

'''
Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
Seen this question in a real interview before?  YesNo

'''


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        results = []
        if not s or not words:
            return results

        wordsDic = {}
        for word in words:
            if word not in wordsDic:
                wordsDic[word] = 0
            wordsDic[word] += 1

        wordL = len(words[0])
        totalL = len(words[0]) * len(words)

        index = 0
        while index < len(s):
            if index + totalL > len(s):
                break
            tempDic = {}
            for word in wordsDic:
                tempDic[word] = wordsDic[word]

            startIndex = index
            for i in range(len(words)):
                subs = s[startIndex:startIndex + wordL]
                if subs not in tempDic:
                    break
                if tempDic[subs] == 0:
                    break
                tempDic[subs] -= 1
                startIndex += wordL
            else:
                results.append(index)
            index += 1
        return results

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    s = "wordgoodstudentgoodword"
    words = ["word", "stud"]
    print(Solution().findSubstring(s,words))