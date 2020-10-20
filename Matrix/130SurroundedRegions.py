# 130. Surrounded Regions
'''
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
from common import *
class Solution:
    '''
    Breath first search to replace all border connected items to 'Y'. Then replace all other 'O's (they are not boarder connected) to 'X' and all 'Y's (they were boarder connected 'O's) to 'O's.
    O(mn) runtime, O(k) storage, in which m and n are rows and columns of the board, k is # of border connected items.
    Beat 97% runtime, 5% storage of all Leetcode submissions.
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0: return
        n = len(board[0])
        if n == 0: return
        border_connected = []
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'Y'
                border_connected.append((i,0))
            if board[i][n-1] == 'O':
                board[i][n-1] = 'Y'
                border_connected.append((i,n-1))
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'Y'
                border_connected.append((0,j))
            if board[m-1][j] == 'O':
                board[m-1][j] = 'Y'
                border_connected.append((m-1,j))
        while border_connected:
            i,j = border_connected.pop()
            if i > 0 and board[i-1][j] == 'O':
                board[i-1][j] = 'Y'
                border_connected.append((i-1,j))
            if i < m-1 and board[i+1][j] == 'O': 
                board[i+1][j] = 'Y'
                border_connected.append((i+1,j))
            if j > 0 and board[i][j-1] == 'O':
                board[i][j-1] = 'Y'
                border_connected.append((i,j-1))
            if j < n-1 and board[i][j+1] == 'O':
                board[i][j+1] = 'Y'
                border_connected.append((i,j+1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

# Tests.
board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
Solution().solve(board)
assert(board == [['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']])
board = [['X','X','X','X'],['X','X','O','X'],['X','O','X','X'],['O','O','X','X']]
Solution().solve(board)
assert(board == [['X','X','X','X'],['X','X','X','X'],['X','O','X','X'],['O','O','X','X']])