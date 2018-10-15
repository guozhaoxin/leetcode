#encoding:utf8
__author__ = 'gold'

'''
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        tempDic = {}

        if not s:
            return

        def dfs(index):
            if index >= len(s):
                return
            if index in tempDic:
                return tempDic[index]
            if index == len(s) - 1:
                tempDic[index] = [[s[index]]]
                return tempDic[index]
            curList = []
            remainList = dfs(index + 1)
            for r in remainList:
                rList = [s[index]]
                rList.extend(r)
                curList.append(rList)
            right = index + 1
            while right < len(s):
                if self.isPar(s,index,right):
                    if right == len(s) - 1:
                        curList.append([s[index:]])
                        break
                    remainList = dfs(right + 1)
                    for r in remainList:
                        rList = [s[index:right + 1]]
                        rList.extend(r)
                        curList.append(rList)
                right += 1

            tempDic[index] = curList
            return tempDic[index]

        results = dfs(0)
        return results


    def isPar(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    s = 'aaaaaaaaaaaaaaaaa'
    result = Solution().partition(s)
    print(result)
    print(len(result))