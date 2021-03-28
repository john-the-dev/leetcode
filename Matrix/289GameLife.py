# 289. Game of Life
'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
'''
from common import *
class Solution:
    '''
    Encode cell which needs update to accomodate 2 values.
    O(mn) runtime, O(1) storage.
    Beat 76% runtime, 44% storage of all Leetcode submissions.
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        oldnew,base,update = {0: 10, 1: 11},10,{10:1,11:0}
        m,n = len(board),len(board[0])
        def getNeighborLiveCount(i, j):
            c = 0
            for k1 in range(-1,2):
                for k2 in range(-1,2):
                    if k1 == 0 and k2 == 0: continue
                    i1,j1 = i+k1,j+k2
                    if i1 >= 0 and i1 < m and j1 >= 0 and j1 < n:
                        v = board[i1][j1]
                        if v > 1: v -= base
                        c += v
            return c
        for i in range(m):
            for j in range(n):
                lives = getNeighborLiveCount(i, j)
                if board[i][j] == 1:
                    if lives < 2 or lives > 3: board[i][j] = oldnew[1]
                else:
                    if lives == 3: board[i][j] = oldnew[0]
        for i in range(m):
            for j in range(n):
                if board[i][j] > 1: board[i][j] = update[board[i][j]]

# Tests.
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
assert(board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
board = [[1,1],[1,0]]
Solution().gameOfLife(board)
assert(board == [[1,1],[1,1]])
