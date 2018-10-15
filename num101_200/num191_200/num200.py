#encoding:utf8
__author__ = 'gold'

'''
Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
'''


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0

        count = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(i - 1,j)
            dfs(i + 1,j)
            dfs(i,j - 1)
            dfs(i, j + 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row,col)

        return count


if __name__ == '__main__':
    # a = [
    #     [1,1,1,1,0],
    # [1,1,0,1,0],
    # [1,1,0,0,0],
    # [0,0,0,0,0]
    # ]
    # print(Solution().numIslands(a))
    #
    # b = [
    #     [1,1,0,0,0],
    #     [1,1,0,0,0],
    #     [0,0,1,0,0],
    # ]
    c = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    c = [["1","0","1","1","0","1","1"]]
    print(Solution().numIslands(c))
    # print(c)
    d = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(Solution().numIslands(d))
    # print(d)