# 200. Number of Islands
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
class Solution:
    '''
    In-storage replacement + DFS.
    O(mn) runtime, O(mn) storage for call stack.
    Beat 99% runtime, 52% storage of all Leetcode submissions.
    '''
    def numIslands(self, grid):
        m = len(grid)
        if m == 0: return 0
        def exploreIsland(i,j):
            grid[i][j] = '0'
            if j > 0 and grid[i][j-1] == '1': exploreIsland(i,j-1)
            if j < n-1 and grid[i][j+1] == '1': exploreIsland(i,j+1)
            if i > 0 and grid[i-1][j] == '1': exploreIsland(i-1,j)
            if i < m-1 and grid[i+1][j] == '1': exploreIsland(i+1,j)
        n,out = len(grid[0]),0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': 
                    out += 1
                    exploreIsland(i,j)
        return out

    '''
    In-storage replacemen + BFS.
    O(mn) runtime, O(min(m,n)) storage. See explanation why it is O(min(m,n)) from smeanionn: https://imgur.com/gallery/M58OKvB.
    Beat 99% runtime, 82% storage of all Leetcode submissions.
    '''
    def numIslands2(self, grid):
        m = len(grid)
        if m == 0: return 0
        n,out = len(grid[0]),0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    layer = set([(i,j)])
                    while layer:
                        new_layer = set() # Use set instead of list. Otherwise, you may add same item more than 1 time.
                        for i1,j1 in layer:
                            grid[i1][j1] = '0'
                            if i1 > 0 and grid[i1-1][j1] == '1': new_layer.add((i1-1,j1))
                            if i1 < m-1 and grid[i1+1][j1] == '1': new_layer.add((i1+1,j1))
                            if j1 > 0 and grid[i1][j1-1] == '1': new_layer.add((i1,j1-1))
                            if j1 < n-1 and grid[i1][j1+1] == '1': new_layer.add((i1,j1+1))
                        layer = new_layer
                    out += 1
        return out

# Tests.
assert(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1)
assert(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3)
assert(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","1","0","0"],
  ["0","0","1","0","0"],
  ["0","1","1","1","1"]
]) == 1)
assert(Solution().numIslands([]) == 0)
assert(Solution().numIslands([["0","1","0","1","0"]]) == 2)
assert(Solution().numIslands([["0"],["1"],["1"],["1"],["0"]]) == 1)

assert(Solution().numIslands2([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1)
assert(Solution().numIslands2([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3)
assert(Solution().numIslands2([
  ["1","1","0","0","0"],
  ["1","1","1","0","0"],
  ["0","0","1","0","0"],
  ["0","1","1","1","1"]
]) == 1)
assert(Solution().numIslands2([]) == 0)
assert(Solution().numIslands2([["0","1","0","1","0"]]) == 2)
assert(Solution().numIslands2([["0"],["1"],["1"],["1"],["0"]]) == 1)