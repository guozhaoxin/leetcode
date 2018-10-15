#encoding:utf8
__author__ = 'gold'

'''
Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = '1'

        if n == 1:
            return s

        count = 1
        s = '1'
        results = ''
        while count < n:
            index = 0
            while index < len(s):
                curIndex = index + 1
                while curIndex < len(s):
                    if s[index] == s[curIndex]:
                        curIndex += 1
                    else:
                        break
                results += str(curIndex - index) + s[index]
                index = curIndex
            count += 1
            s = results
            results = ''
        return s
if __name__ == '__main__':
    print(Solution().countAndSay(6))