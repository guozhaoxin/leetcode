#encoding:utf8
__author__ = 'gold'

'''
Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        maxL = 0

        height = len(matrix)
        width = len(matrix[0])

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '0':
                    continue
                bottom = i + 1
                right = j + 1
                while bottom < height and right < width:
                    index = j
                    while index <= right and matrix[bottom][index] == '1':
                        index += 1
                    if index <= right:
                        break
                    index = i
                    while index <= bottom and matrix[index][right] == '1':
                        index += 1
                    if index <= bottom:
                        break
                    bottom += 1
                    right += 1
                maxL = max(bottom - i,maxL)

        return maxL ** 2


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        M = len(matrix)
        if not M:
            return 0
        N = len(matrix[0])

        maxSize, vec = 0, [0] * N
        for i in range(M):
            for j in range(N):
                vec[j] = 0 if matrix[i][j] == '0' else vec[j] + 1  ## 记录连'1'长度

            count = 0
            for k in range(N):
                if vec[k] > maxSize:
                    count += 1
                    if count > maxSize:
                        maxSize += 1
                        break
                else:
                    count = 0

        return maxSize ** 2


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        widths = [0] * n
        k = 0
        for j in range(m):
            max_continous_k = 0
            continous_k = 0
            for i in range(n):
                if matrix[i][j] == '1':
                    widths[i] += 1
                else:
                    widths[i] = 0
                if widths[i] > k:
                    continous_k += 1
                    max_continous_k = max(max_continous_k,continous_k)
                else:
                    continous_k = 0
            if max_continous_k > k:
                k += 1
        return k*k

if __name__ == '__main__':
    array = [
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0'],
    ]
    print(Solution().maximalSquare(array))