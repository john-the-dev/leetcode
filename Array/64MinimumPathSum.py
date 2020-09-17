# 64. Minimum Path Sum
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
import sys
class Solution:
    '''
    Classic dynamic programming, dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1])+grid[i][j]
    O(mn) runtime, O(mn) storage.
    Beat 98% runtime, 34% storage of all Leetcode submissions.
    '''
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        dp = [[sys.maxsize for j in range(n+1)] for i in range(m+1)]
        dp[1][0],dp[0][1] = 0,0
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1])+grid[i][j]
        return dp[m][n]

# Tests.
assert(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7)
assert(Solution().minPathSum([]) == 0)
assert(Solution().minPathSum([[1,3,1]]) == 5)
assert(Solution().minPathSum([[1],[3],[1]]) == 5)
assert(Solution().minPathSum([[1,3,8],[5,1,1],[4,2,1]]) == 7)