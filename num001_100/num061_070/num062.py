#encoding:utf8
__author__ = 'gold'

'''
Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 1 or n == 1:
            return 1

        return self.jiecheng(m + n - 2) // (self.jiecheng(m - 1) * self.jiecheng(n - 1))

    def jiecheng(self,num):
        if num == 1:
            return 1

        mul = 1
        for i in range(2,num + 1):
            mul *= i

        return mul

class Solution1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        results = [[0 for i in range(n)] for j in range(m)]
        results[0][0] = 1

        for i in range(m):
            for j in range(n):
                if j > 0:
                    results[i][j] += results[i][j - 1]
                if i > 0:
                    results[i][j] += results[i - 1][j]
        return results[-1][-1]

if __name__ == '__main__':
    print(Solution().uniquePaths(100,100))
    print(Solution1().uniquePaths(100,100))