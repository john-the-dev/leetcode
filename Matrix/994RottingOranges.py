# 994. Rotting Oranges
'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''
from common import *
class Solution:
    '''
    Breath first search.
    O(mn) runtime, O(mn) storage.
    Beat 99% runtime, 5% storage of all Leetcode submissions.
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        out,layer = 0,set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: layer.add((i,j))
        while layer:
            new_layer,out = set(),out+1
            for i1,j1 in layer:
                grid[i1][j1] = 0
            for i1,j1 in layer:
                if i1 > 0 and grid[i1-1][j1] > 0: new_layer.add((i1-1,j1))
                if i1 < m-1 and grid[i1+1][j1] > 0: new_layer.add((i1+1,j1))
                if j1 > 0 and grid[i1][j1-1] > 0: new_layer.add((i1,j1-1))
                if j1 < n-1 and grid[i1][j1+1] > 0: new_layer.add((i1,j1+1))
            layer = new_layer
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return out-1 if out >= 1 else 0

assert(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4)
assert(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1)
assert(Solution().orangesRotting([[0,2]]) == 0)
assert(Solution().orangesRotting([[2,1,1],[1,2,0],[0,1,1]]) == 2)
assert(Solution().orangesRotting([[0],[2]]) == 0)
assert(Solution().orangesRotting([[0]]) == 0)
assert(Solution().orangesRotting([[0,2,2]]) == 0)
                    