# 279. Perfect Squares
'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
    '''
    Dynamic programming, dp[i] = min(dp[i-1],dp[i-4],dp[i-9],...)
    O(n^1.5) runtime, O(n) storage.
    Beat 23% runtime, 41% storage of all Leetcode submissions.
    '''
    def numSquares(self, n):
        dp = [0]*(n+1)
        for i in range(1,n+1):
            for k in range(1,int(i**0.5)+1):
                prev = dp[i-k**2]
                if dp[i] == 0 or dp[i] > prev+1: dp[i] = prev+1
        return dp[n]

# Tests.
assert(Solution().numSquares(1) == 1)
assert(Solution().numSquares(2) == 2)
assert(Solution().numSquares(3) == 3)
assert(Solution().numSquares(4) == 1)
assert(Solution().numSquares(12) == 3)
assert(Solution().numSquares(13) == 2)
