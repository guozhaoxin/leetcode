#encoding:utf8
__author__ = 'gold'

'''
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        def digui(row,column,orderdDic,index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or column >= len(board[0]) or column < 0:
                return False
            curKey = (row,column)
            if curKey in orderdDic.keys() or board[row][column] != word[index]:
                return False
            newDic = orderdDic.copy()
            newDic[curKey] = 1
            return digui(row + 1,column,newDic,index + 1) or digui(row - 1,column,newDic,index + 1) or digui(row,column - 1,newDic,index + 1) or digui(row,column + 1,newDic,index + 1)

        for row in range(len(board)):
            for column in range(len(board[0])):
                result = digui(row,column,{},0)
                if result:
                    return True

        return False

if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
        ['D','E','S','F']
    ]
    board = [['a']]
    print(Solution().exist(board,'ab'))