# 773. Sliding Puzzle
'''
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
'''
from common import *
import sys
import heapq
class Solution:
    '''
    Dijkstra's algorithm.
    O(64^2log(64)) runtime, O(64) storage.
    Beat 45% runtime, 100% storage of all Leetcode submissions.
    '''
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        stop_status,moves = 123450,{}
        def getIndex(board,normalized=False):
            out = 0
            if normalized:
                for i in range(6):
                    out *= 10
                    out += board[i]
            else:
                for i in range(2):
                    for j in range(3):
                        out *= 10
                        out += board[i][j]
            return out
        def getNextIndexes(index):
            board = list('%06d' % index)
            for i in range(6):
                board[i] = int(board[i])
            i = 0
            while board[i] != 0:
                i += 1
            out = []
            j1,j2,j3 = i-1,i+1,i+3
            if j1 >= 0 and j1 != 2:
                board[j1],board[i] = board[i],board[j1]
                out.append(getIndex(board,True))
                board[j1],board[i] = board[i],board[j1]
            if j2 < 6 and j2 != 3:
                board[j2],board[i] = board[i],board[j2]
                out.append(getIndex(board,True))
                board[j2],board[i] = board[i],board[j2]
            if j3 >= 6: j3 -= 6
            board[j3],board[i] = board[i],board[j3]
            out.append(getIndex(board,True))
            board[j3],board[i] = board[i],board[j3]
            return out
        i = getIndex(board)
        moves[i] = 0
        q = [(0,i)]
        while q:
            move,i = heapq.heappop(q)
            if i == stop_status: return move
            indexes = getNextIndexes(i)
            for j in indexes:
                if j not in moves: moves[j] = sys.maxsize
                if move+1 < moves[j]:
                    heapq.heappush(q,(move+1,j))
                    moves[j] = move+1
        return -1

    '''
    Classic BFS
    O(6!) runtime, O(6!) storage.
    Beat 94% runtime, 100% storage of Leetcode submissions.
    '''
    def slidingPuzzle2(self, board: List[List[int]]) -> int:
        def board2tuple(board):
            out = []
            for i in range(2):
                for j in range(3):
                    out.append(board[i][j])
            return tuple(out)
        def getnext(t):
            arr = list(t)
            i = 0
            while i < 6 and t[i] != 0:
                i += 1
            temp,out = [],[]
            j = i+1
            if j != 3 and j != 6: temp.append(j)
            j = i-1
            if j != -1 and j != 2: temp.append(j)
            temp.append((i+3) % 6)
            for j in temp:
                arr[i],arr[j] = arr[j],arr[i]
                out.append(tuple(arr))
                arr[i],arr[j] = arr[j],arr[i]
            return out
        start = board2tuple(board)
        layer = [start]
        seen,out,win = set(layer),0,(1,2,3,4,5,0)
        if start == win: return out
        while layer:
            new_layer,out = [],out+1
            for val in layer:
                for item in getnext(val):
                    if item == win: return out
                    if item not in seen: 
                        new_layer.append(item)
                        seen.add(item)
            layer = new_layer
        return -1


# Tests.
assert(Solution().slidingPuzzle([[1,2,3],[4,0,5]]) == 1)
assert(Solution().slidingPuzzle([[1,2,3],[5,4,0]]) == -1)
assert(Solution().slidingPuzzle([[4,1,2],[5,0,3]]) == 5)
assert(Solution().slidingPuzzle2([[1,2,3],[4,0,5]]) == 1)
assert(Solution().slidingPuzzle2([[1,2,3],[5,4,0]]) == -1)
assert(Solution().slidingPuzzle2([[4,1,2],[5,0,3]]) == 5)
assert(Solution().slidingPuzzle2([[3,2,4],[1,5,0]]) == 14)