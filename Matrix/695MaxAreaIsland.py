# 695. Max Area of Island
'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
from common import *
class Solution:
    '''
    BFS + in-storage replacement.
    O(mn) runtime, O(m+n) storage.
    Beat 97% runtime, 92% storage of all Leetcode submissions.
    Note: it also can be solved with DFS with same complexity.
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        out = 0
        def bfs(i1, j1):
            nonlocal out
            pool,total = [(i1,j1)],0
            while pool:
                new_pool = []
                for i,j in pool:
                    total += 1
                    if i > 0 and grid[i-1][j] == 1: 
                        grid[i-1][j] = 0
                        new_pool.append((i-1,j))
                    if i < m-1 and grid[i+1][j] == 1: 
                        grid[i+1][j] = 0
                        new_pool.append((i+1,j))
                    if j > 0 and grid[i][j-1] == 1: 
                        grid[i][j-1] = 0
                        new_pool.append((i,j-1))
                    if j < n-1 and grid[i][j+1] == 1: 
                        grid[i][j+1] = 0
                        new_pool.append((i,j+1))
                pool = new_pool
            out = max(out,total)
        for i1 in range(m):
            for j1 in range(n):
                if grid[i1][j1] == 1: 
                    grid[i1][j1] = 0
                    bfs(i1,j1)
        return out

# Tests.
assert(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6)
assert(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0)
assert(Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]) == 4)
