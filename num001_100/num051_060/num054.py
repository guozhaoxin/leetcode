#encoding:utf8
__author__ = 'gold'

'''
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        results = []

        if not matrix:
            return results

        rowEnd = len(matrix) #每次循环时最下边行的索引 + 1
        columnEnd = len(matrix[0]) #每次循环时最右边列的索引 + 1

        curFirstRow = 0 #每次循环时第一行的索引
        curFirstColumn = 0 #每次循环时第一列的索引

        while curFirstRow < rowEnd and curFirstColumn < columnEnd:
            for column in range(curFirstColumn,columnEnd):
                results.append(matrix[curFirstRow][column])
            if curFirstRow == rowEnd - 1:
                break

            for row in range(curFirstRow + 1,rowEnd):
                results.append(matrix[row][columnEnd - 1])
            if columnEnd - 1 == curFirstColumn:
                break

            for column in range(columnEnd - 2,curFirstColumn - 1,-1):
                results.append(matrix[rowEnd - 1][column])
            if rowEnd - 1 == curFirstRow:
                break

            for row in range(rowEnd - 2,curFirstRow,-1):
                results.append(matrix[row][curFirstColumn])

            curFirstRow += 1
            rowEnd -= 1
            curFirstColumn += 1
            columnEnd -= 1

        return results

if __name__ == '__main__':
    s = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    # s = [
  # [1, 2, 3, 4],
  # [5, 6, 7, 8],
  # [9,10,11,12]
# ]
    # s = [[2,5,8],[4,0,-1]]
    print(Solution().spiralOrder(s))