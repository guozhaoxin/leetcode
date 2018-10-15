#encoding:utf8
__author__ = 'gold'

'''
Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix:
            return

        firstRow = False

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                firstRow = True
            for column in range(1,len(matrix[0])):
                if matrix[row][column] == 0:
                    matrix[row][0] = matrix[0][column] = 0

        for row in range(len(matrix) - 1,-1,-1):
            for column in range(len(matrix[0]) - 1,0,-1):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0
            if firstRow:
                matrix[row][0] = 0

def p(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    matrix = [
  [1,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    Solution().setZeroes(matrix)
    p(matrix)