#encoding:utf8
__author__ = 'gold'

'''
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if s[0] != '0' else 0

        resultList = [0 for i in range(len(s) + 1)] #保存每一位的结果
        if s[-1] != '0':
            resultList[-2] = 1
        resultList[-1] = 1
        index = len(s) - 2
        while index > 0:
            if s[index] == '0':
                resultList[index] = 0
            else:
                num = int(s[index:index + 2])
                if num > 0 and num < 27:
                    resultList[index] = resultList[index + 1] + resultList[index + 2]
                else:
                    resultList[index] = resultList[index + 1]
            index -= 1

        if s[0] == '0':
            resultList[0] = 0
        else:
            num = int(s[0:2])
            if num > 0 and num < 27:
                resultList[0] = resultList[1] + resultList[2]
            else:
                resultList[0] = resultList[1]
        # print(resultList)
        return resultList[0]

from collections import defaultdict
class Solution:
    def numDecodings(self, message):
        """
        :type s: str
        :rtype: int
        """
        message_size = len(message)

        cache = defaultdict(int)
        cache[message_size] = 1

        for i in reversed(range(message_size)):
            if message[i].startswith('0'):
                cache[i] = 0
            elif i == message_size - 1:
                cache[i] = 1
            else:
                if int(message[i:i + 2]) <= 26:
                    cache[i] = cache[i + 2]
                cache[i] += cache[i + 1]

        return cache[0]


if __name__ == '__main__':
    # print(Solution().numDecodings("12"))
    # print(Solution().numDecodings("226"))
    # print(Solution().numDecodings("2"))
    print(Solution().numDecodings("100"))
    # print(Solution().numDecodings("1234"))
    # print(Solution().numDecodings("1111111111111111111"))
    # print(Solution().numDecodings("0002"))
    # print(Solution().numDecodings("02"))