#encoding:utf8
__author__ = 'gold'

'''
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        minSumGrid = [[grid[i][j] for j in range(n)] for i in range(m)]
        # minSumGrid[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j > 0:
                        minSumGrid[i][j] += minSumGrid[i][j - 1]
                elif j == 0:
                    minSumGrid[i][j] += minSumGrid[i - 1][j]
                else:
                    minSum = min(minSumGrid[i-1][j],minSumGrid[i][j - 1])
                    minSumGrid[i][j] += minSum

        return minSumGrid[-1][-1]

if __name__ == '__main__':
    s = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    res = Solution().minPathSum(s)
    print(res)