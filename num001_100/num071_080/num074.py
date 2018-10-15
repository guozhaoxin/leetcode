#encoding:utf8
__author__ = 'gold'

'''
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        if row == 0:
            return False

        col = len(matrix[0])
        if col == 0:
            return False

        index = 0
        while index < row:
            if matrix[index][-1] > target:
                break
            elif matrix[index][-1] == target:
                return True

            if index < row - 1:
                if matrix[index + 1][0] <= target:
                    index += 1
                else:
                    return False
            else:
                return False

        if index >= row:
            return False

        low = 0
        high = col - 1
        while low <= high:
            mid = (high + low) // 2
            if matrix[index][mid] == target:
                return True
            if matrix[index][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 100
    print(Solution().searchMatrix(matrix,target))
    print(Solution().searchMatrix([[1]],1))
