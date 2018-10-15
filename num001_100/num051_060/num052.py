#encoding:utf8
__author__ = 'gold'

'''
N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2 or n == 3:
            return 0

        Q = 'Q'
        dot = '.'
        def digui(sortedArray):
            # print(sortedArray)
            if len(sortedArray) == n:
                temp = []
                for i in range(n):
                    QPos = [dot] * n
                    QPos[sortedArray[i]] = Q
                    temp.append(''.join(QPos))
                results.append(temp)

            else:
                for i in range(n):
                    if not sortedArray:
                        digui([i])
                    else:
                        hAix = len(sortedArray)
                        for j in range(len(sortedArray)):
                            if i == sortedArray[j] or (abs(hAix - j) == abs(sortedArray[j] - i)):
                                break
                        else:
                            digui(sortedArray + [i])

        results = []
        digui([])
        return len(results)
