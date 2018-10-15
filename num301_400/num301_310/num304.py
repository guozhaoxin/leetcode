#encoding:utf8
__author__ = 'gold'

'''
304.Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.sumTable = [[0]]
        else:
            self.sumTable = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    self.sumTable[row + 1][col + 1] = self.sumTable[row + 1][col] + self.sumTable[row][col + 1] + self.matrix[row][col] - self.sumTable[row][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumTable[row2 + 1][col2 + 1] - self.sumTable[row1][col2 + 1] - self.sumTable[row2 + 1][col1] + self.sumTable[row1][col1]