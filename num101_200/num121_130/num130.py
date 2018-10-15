#encoding:utf8
__author__ = 'gold'

'''
Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        height = len(board)
        width = len(board[0])
        def dfs(board, y, x):
            if x < 0 or x >= width or y < 0 or y >= height or board[y][x] != 'O':
                return
            board[y][x] = 'S'
            dfs(board, y + 1, x)
            dfs(board, y - 1, x)
            dfs(board, y, x + 1)
            dfs(board, y, x - 1)
        for i in range(width):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[height-1][i] == 'O':
                dfs(board, height-1, i)
        for j in range(height):
            if board[j][0] == 'O':
                dfs(board, j, 0)
            if board[j][width-1] == 'O':
                dfs(board, j, width-1)
        for y in range(height):
            for x in range(width):
                if board[y][x] == 'S':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'

def p(board):
    for b in board:
        print(b)

if __name__ == '__main__':
    # board = [
    #     ['X', 'X', 'X', 'X'],
    #     ['X', 'O', 'O', 'X'],
    #     ['X','X','O', 'X'],
    #     ['X','O','X', 'X']
    # ]
    # for b in board:
    #     print(b)
    # Solution().solve(board)
    # print('*******')
    # for b in board:
    #     print(b)

    print('*****')
    board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    p(board)
    Solution().solve(board)
    print('*****')
    p(board)