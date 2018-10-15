#encoding:utf8
__author__ = 'gold'

'''
 Pascal's Triangle
 
 Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        results = []
        if numRows == 0:
            return results

        results.append([1])
        if numRows == 1:
            return results

        results.append([1,1])
        if numRows == 2:
            return results

        row = 3
        while row <= numRows:
            results.append([1 for i in range(row)])
            index = 1
            while index < row - 1:
                results[-1][index] = results[-2][index-1] + results[-2][index]
                index += 1
            row += 1

        return results

if __name__ == '__main__':
    print(Solution().generate(5))