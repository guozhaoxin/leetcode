#encoding:utf8
__author__ = 'gold'

'''
Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        self.wordSet = wordDict

        def dfs(index):
            if index == len(s) - 1:
                if s[index] in self.wordSet:
                    return True
                return False

            if s[index:] in self.wordSet:
                return True

            # while index < len(s):
            endIndex = index
            while endIndex < len(s):
                if s[index:endIndex + 1] in self.wordSet:
                    subResult = dfs(endIndex + 1)
                    if subResult:
                        return True
                endIndex += 1
            return False
        return dfs(0)


class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(0, i):
                print(i,j)
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]  # or dp[n]


from collections import deque


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #         wordDist = set(wordDict)
        #         f = [False]*(len(s)+1)

        #         f[0] = True

        #         for i in range(1, len(s)+1):
        #             f[i] = next((True for j in range(i) if f[j] and s[j:i] in wordDict), False)
        #             # for j in range(i):
        #             #     if f[j] and s[j:i] in wordDict:
        #             #         f[i] = True
        #             #         break
        #         return f[len(s)]

        #         if s == None or wordDict == None:
        #             return False

        if wordDict == [] or wordDict == set():
            return s == ""

        dic = set()
        minlen, maxlen = float("inf"), 1
        for word in wordDict:
            if word != "":
                dic.add(word)
                if len(word) < minlen:
                    minlen = len(word)
                if len(word) > maxlen:
                    maxlen = len(word)

        dp = deque([0])  # indices where s[:dp[i]] can be expressed by wordDict

        for i in range(minlen, len(s) + 1):
            for j in dp:
                print(j)
                if i - j > maxlen:
                    break
                if s[j:i] in dic:
                    dp.appendleft(i)
                    break

        return dp[0] == len(s)


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]

    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]

    # s = "aaaaaaa"
    # wordDict = ["aaaa", "aaa"]

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

    print(Solution().wordBreak(s,wordDict))