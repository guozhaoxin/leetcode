#encoding:utf8
__author__ = 'gold'

'''
Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        results = []

        if k == 0:
            return results

        if n < k:
            return results

        # numList = [i for i in range(n)]

        def digui(start,curList):
            if len(curList) == k:
                results.append(curList)
                return

            for index in range(start + 1,n):
                digui(index,curList + [index + 1])

        for i in range(n):
            digui(i,[i + 1])
        return results

if __name__ == '__main__':
    results = Solution().combine(5,1)
    print(results)
    print(len(results))