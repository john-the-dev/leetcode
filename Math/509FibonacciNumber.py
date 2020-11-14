# 509. Fibonacci Number
'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
'''
from common import *
class Solution:
    '''
    Recursion.
    O(2^N) runtime, O(N) storage.
    Beat 23% runtime, 59% storage of all Leetcode submissions.
    '''
    def fib(self, N: int) -> int:
        if N <= 1: return N
        return self.fib(N-1) + self.fib(N-2)

    '''
    DP based solution.
    O(N) runtime, O(N) storage.
    Beat 93% runtime, 59% storage of all Leetcode submissions.
    '''
    def fib2(self, N: int) -> int:
        dp = [0]*(N+1)
        if N >= 1: dp[1] = 1
        for i in range(2,N+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[N]

    '''
    Improve storage with dp.
    O(N) runtime, O(1) storage.
    Beat 78% runtime, 59% storage of all Leetcode submissions.
    '''
    def fib3(self, N: int) -> int:
        if N <= 1: return N
        prev0,prev1 = 0,1
        for _ in range(2,N+1):
            curr = prev0+prev1
            prev0,prev1 = prev1,curr
        return curr

# Tests.
assert(Solution().fib(2) == 1)
assert(Solution().fib(3) == 2)
assert(Solution().fib(4) == 3)
assert(Solution().fib(5) == 5)
assert(Solution().fib2(2) == 1)
assert(Solution().fib2(3) == 2)
assert(Solution().fib2(4) == 3)
assert(Solution().fib2(5) == 5)
assert(Solution().fib3(2) == 1)
assert(Solution().fib3(3) == 2)
assert(Solution().fib3(4) == 3)
assert(Solution().fib3(5) == 5)