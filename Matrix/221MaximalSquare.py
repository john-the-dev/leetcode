# 221. Maximal Square
'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''
from common import *
class Solution:
    '''
    Dynamic programming: dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1 if matrix[i][j] == '1' else 0
    O(mn) runtime, O(mn) storage.
    Beat 36% runtime, 52% storage of all Leetcode submissions.
    '''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        out = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    upper = min(dp[i][j],dp[i][j+1])
                    left = min(dp[i][j],dp[i+1][j])
                    dp[i+1][j+1] = min(upper+1,left+1)
                    out = max(dp[i+1][j+1],out)
        return out*out

# Tests.
assert(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4)
assert(Solution().maximalSquare([["0","1"],["1","0"]]) == 1)
assert(Solution().maximalSquare([["0"]]) == 0)