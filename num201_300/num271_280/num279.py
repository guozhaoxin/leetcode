#encoding:utf8
__author__ = 'gold'

'''
279.
Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        mi = n ** .5
        if int(mi) ** 2 == n:
            return 1

        squareList = []
        i = 1
        haha = i ** 2
        while haha <= n:
            squareList.append(haha)
            i += 1
            haha = i ** 2

        self.sumCount = n

        def dfs(curCount,leftSum):

            if curCount + 1 >= self.sumCount and leftSum != 0:
                return

            if leftSum == 0:
                self.sumCount = min(self.sumCount,curCount)
                return

            for index in range(len(squareList) - 1,-1,-1):
                if leftSum < squareList[index]:
                    continue
                dfs(curCount + 1,leftSum - squareList[index])

        dfs(0,n)
        return self.sumCount

if __name__ == '__main__':
    # print(Solution().numSquares(13))
    print(Solution().numSquares(12))
    # print(Solution().numSquares(16))
    # print(Solution().numSquares(2))
    # print(Solution().numSquares(5))
    # print(Solution().numSquares(6))
    # print(Solution().numSquares(7))
    # print(Solution().numSquares(8))