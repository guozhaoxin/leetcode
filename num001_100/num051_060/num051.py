#encoding:utf8
__author__ = 'gold'

'''
N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        if n == 0:
            return []
        if n == 1:
            return [['Q']]
        if n == 2 or n == 3:
            return []

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
        return results

def p(arrayArray):
    for x in arrayArray:
        for y in x:
            print(y)
        print('*************')

if __name__ == '__main__':
    results = Solution().solveNQueens(4)
    p(results)
    print(len(results))
