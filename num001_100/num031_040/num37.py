#encoding:utf8
__author__ = 'gold'

'''
Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        globalDic = {}
        def digui(row,col):
            if row == 9:
                return True
            if col == 9:
                return digui(row + 1,0)
            else:
                if board[row][col] == '.':
                    nums = set('123456789')
                    for i in range(9):
                        element = board[row][i]
                        if element in nums:
                            nums.remove(element)
                    for j in range(9):
                        element = board[j][col]
                        if element in nums:
                            nums.remove(element)
                    gridR = row // 3
                    gridC = col // 3

                    for r in range(gridR * 3,gridR * 3 + 3):
                        for c in range(gridC * 3,gridC * 3 + 3):
                            element = board[r][c]
                            if board[r][c] in nums:
                                nums.remove(element)
                    if not nums:
                        return False
                    else:
                        for element in nums:
                            globalDic[(row,col)] = element
                            board[row][col] = element
                            result = digui(row,col + 1)
                            if not result:
                                board[row][col] = '.'
                                globalDic.pop((row,col))
                            else:
                                return True
                else:
                    return digui(row,col + 1)
        digui(0,0)
#
if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    Solution().solveSudoku(board)
    for s in board:
        print(s)