#encoding:utf8
__author__ = 'gold'

'''
467.
Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab
'''


class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        alpNeiDic = {
            'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l',
            'l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w',
            'w':'x','x':'y','y':'z','z':'a'
        }
        tempSet = set() #保存所有中间结果

        left = 0
        results = 0
        while left < len(p):
            right = left + 1
            while right < len(p):
                if alpNeiDic[p[right - 1]] != p[right]:
                    break
                right += 1
            while left < right:
                tempIndex = left + 1
                while tempIndex <= right:
                    pass


            left = right #right指向的是下一个非连续的单词

        return results


class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        alpNeiDic = {
            'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l',
            'l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w',
            'w':'x','x':'y','y':'z','z':'a'
        }
        tempSet = set() #保存所有中间结果

        left = 0
        results = 0
        while left < len(p):
            if p[left] not in tempSet:
                results += 1
                tempSet.add(p[left])
            right = left + 1
            while right < len(p) and p[right] == alpNeiDic[p[right - 1]]:
                if p[left:right + 1] not in tempSet:
                    results += 1
                    tempSet.add(p[left:right + 1])
                right += 1
            left += 1
        return results

if __name__ == '__main__':
    s = "ghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    print(Solution().findSubstringInWraproundString(s))
    print(Solution().findSubstringInWraproundString('a'))