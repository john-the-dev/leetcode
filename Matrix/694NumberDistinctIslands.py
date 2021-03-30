# 694. Number of Distinct Islands
'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
'''
from common import *
class Solution:
    '''
    Relative position to left upper position of an island. Positon sequence to hash as signature. In-storage replacement to avoid repeat counting.
    O(mn) runtime, O(mn) storage.
    Beat 98% runtime, 92% storage of all Leetcode submissions.
    '''
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen,m,n = set(),len(grid),len(grid[0])
        def exploreIsland(i, j):
            nonlocal seen
            grid[i][j] = 0
            seq = [(0,0)]
            layer = [(i,j)]
            while layer:
                new_layer = []
                for i1,j1 in layer:
                    if i1 > 0 and grid[i1-1][j1] == 1: 
                        grid[i1-1][j1] = 0
                        seq.append((i1-1-i,j1-j))
                        new_layer.append((i1-1,j1))
                    if i1 < m-1 and grid[i1+1][j1] == 1:
                        grid[i1+1][j1] = 0
                        seq.append((i1+1-i,j1-j))
                        new_layer.append((i1+1,j1))
                    if j1 > 0 and grid[i1][j1-1] == 1:
                        grid[i1][j1-1] = 0
                        seq.append((i1-i,j1-1-j))
                        new_layer.append((i1,j1-1))
                    if j1 < n-1 and grid[i1][j1+1] == 1:
                        grid[i1][j1+1] = 0
                        seq.append((i1-i,j1+1-j))
                        new_layer.append((i1,j1+1))
                layer = new_layer
            seen.add(hash(str(seq))) 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: exploreIsland(i, j)
        return len(seen)

# Tests.
assert(Solution().numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]) == 1)
assert(Solution().numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]) == 3)
