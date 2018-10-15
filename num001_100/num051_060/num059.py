#encoding:utf8
__author__ = 'gold'

'''
Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        results = []
        if n == 0:
            return results
        if n == 1:
            return [[1]]

        for i in range(n):
            results.append([1] * n)

        curNum = 1

        curFirstRow = 0
        curFirstColumn = 0
        curLastRow = n - 1
        curLastColumn = n - 1

        while curFirstRow < curLastRow:
            for column in range(curFirstColumn,curLastColumn + 1):
                results[curFirstRow][column] = curNum
                curNum += 1

            for row in range(curFirstRow + 1,curLastRow + 1):
                results[row][curLastColumn] = curNum
                curNum += 1

            for column in range(curLastColumn - 1,curFirstColumn - 1,-1):
                results[curLastRow][column] = curNum
                curNum += 1

            for row in range(curLastRow - 1,curFirstRow,-1):
                results[row][curFirstColumn] = curNum
                curNum += 1

            curFirstColumn += 1
            curFirstRow += 1
            curLastRow -= 1
            curLastColumn -= 1
        if n % 2 == 1:
            results[n // 2][n //2] = n * n
        return results

if __name__ == '__main__':
    print(Solution().generateMatrix(2))
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))
    print(Solution().generateMatrix(5))