#encoding:utf8
__author__ = 'gold'

'''
Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        height = len(matrix)
        width = len(matrix[0])
        if width == 0:
            return False

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        column = 0
        while column < width:
            top = 0
            bottom = height - 1
            if matrix[top][column] == target or matrix[bottom][column] == target:
                return True
            if matrix[top][column] > target:
                return False
            if matrix[bottom][column] < target:
                column += 1
                continue
            while bottom >= top:
                mid = (bottom + top) // 2
                if matrix[mid][column] == target:
                    return True
                if matrix[mid][column] < target:
                    top = mid + 1
                else:
                    bottom = mid - 1
            if column == width - 1:
                return False
            if matrix[-1][column] < matrix[0][column + 1]:
                return False
            column += 1

        return False


class Solution(object):
    def searchMatrix(self, matrix, target):
        j = -1
        for row in matrix:
            while j + len(row) >= 0 and row[j] > target:
                j -= 1
            if j + len(row) >= 0 and row[j] == target:
                return True
        return False


if __name__ == '__main__':
    nums = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    print(Solution().searchMatrix(nums,5))
    print(Solution().searchMatrix(nums,20))
    print(Solution().searchMatrix([[]],20))
    print(Solution().searchMatrix([[-1,3]],3))