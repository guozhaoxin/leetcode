#encoding:utf8
__author__ = 'gold'

'''
Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return 0

        maxArea = 0
        rowIndex = 0
        while rowIndex < row:
            colIndex = 0
            while colIndex < col:
                while colIndex < col and matrix[rowIndex][colIndex] == '0':
                    colIndex += 1
                if colIndex == col:
                    break
                preFlag = colIndex
                while preFlag < col and matrix[rowIndex][preFlag] == '1':
                    preFlag += 1
                maxArea = max(maxArea,preFlag - colIndex)
                lastRow = rowIndex + 1
                while lastRow < row:
                    if matrix[lastRow][colIndex] == '0':
                        break
                    lastCol = colIndex
                    while lastCol < col:
                        if matrix[lastRow][lastCol] == '0':
                            maxArea = max(maxArea,(lastCol - colIndex),(lastRow - rowIndex + 1),(lastRow - rowIndex + 1) * (min(preFlag,lastCol) - colIndex))
                            preFlag = min(preFlag,lastCol)
                            break
                        lastCol += 1
                    if lastCol == col:
                        maxArea = max(maxArea, (lastCol - colIndex), (lastRow - rowIndex + 1),
                                      (lastRow - rowIndex + 1) * (min(preFlag, lastCol) - colIndex))
                    lastRow += 1
                colIndex += 1

            rowIndex += 1
        return maxArea


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        nums = [int(''.join(row), base=2) for row in matrix]
        print(nums)

        max_area = 0
        for i in range(len(nums)):
            j = i
            num = nums[i]
            while j < len(nums):
                # print(num, nums[j])
                num = num & nums[j]
                if num == 0:
                    break
                cur_num = num
                l = 0
                # print i,j,cur_num
                while cur_num != 0:
                    l += 1
                    cur_num = cur_num & (cur_num << 1)
                    # print(cur_num)
                max_area = max(max_area, l * (j - i + 1))
                j += 1

        return max_area

if __name__ == '__main__':
    matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

    matrix = [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
    # print(matrix)
    matrix = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
    print(Solution().maximalRectangle(matrix))