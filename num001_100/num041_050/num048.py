#encoding:utf8
__author__ = 'gold'

'''
Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix) #获得每个维度的长
        startIndex = 0 #标记每转一个圈时左上角第一个元素的索引（双维）
        while l > 1:
            endIndex = startIndex + l

            #先换四个角的数据
            temp = matrix[startIndex][endIndex - 1]
            matrix[startIndex][endIndex - 1] = matrix[startIndex][startIndex]
            temp2 = matrix[endIndex - 1][endIndex - 1]
            matrix[endIndex - 1][endIndex - 1] = temp
            temp = matrix[endIndex - 1][startIndex]
            matrix[endIndex - 1][startIndex] = temp2
            matrix[startIndex][startIndex] = temp

            #先转换第一条横边
            temp = []
            for i in range(startIndex + 1,endIndex - 1):
                temp.append(matrix[i][endIndex - 1]) #保存的数顺序在原始中为从上到下
            for i in range(startIndex + 1,endIndex- 1):
                matrix[i][endIndex - 1] = matrix[startIndex][i]

            #再转换右侧的竖边
            temp2 = []
            for i in range(startIndex + 1,endIndex - 1):
                temp2.append(matrix[endIndex - 1][i])
            for i in range(startIndex + 1,endIndex - 1):
                matrix[endIndex - 1][i] = temp[-1]
                temp.pop(-1)

            #再转换下边的横边
            temp = []
            for i in range(startIndex + 1,endIndex - 1):
                temp.append(matrix[i][startIndex])
            index = 0
            for i in range(startIndex + 1,endIndex - 1):
                matrix[i][startIndex] = temp2[index]
                index += 1

            #转换左边的竖边
            for i in range(startIndex + 1,endIndex - 1):
                matrix[startIndex][i] = temp[-1]
                temp.pop(-1)
            startIndex += 1
            l -= 2

def p(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    matrix = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
    # matrix = [
    #     [1,2],
    #     [3,4]
    # ]
    # matrix = []
    import random
    matrix = []
    for i in range(6):
        temp = []
        for j in range(6):
            temp.append(random.randint(0,20))
        matrix.append(temp)
    p(matrix)
    Solution().rotate(matrix)
    print('****')
    p(matrix)