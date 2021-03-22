# 829. Consecutive Numbers Sum
'''
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
'''
from common import *
import math
class Solution:
    '''
    Math: For any solution, (low+high)k/2=N -> (low+low+k-1)k/2=N -> low = (2N+k-k*k)/2k.
    O(N^0.5) runtime, O(1) storage.
    Beat 46% runtime, 99.9% storage of all Leetcode submissions.
    '''
    def consecutiveNumbersSum(self, N: int) -> int:
        k,out = 1,0
        while True:
            val = (2*N+k-k*k)
            if val < 2*k: break
            if val % (2*k) == 0: out += 1
            k += 1
        return out

    '''
    Math: assuming k consecutive #s as a solution, then then N/k must be either ####.5 or ####.0 depending on whether k is even or not.
    O(N^0.5) runtime, O(1) storage.
    Beat 22% runtime, 74% storage of all Leetcode submissions.
    '''
    def consecutiveNumbersSum2(self, N: int) -> int:
        out,k = 0,1
        while True:
            v = N / k
            if v - k // 2 <= 0: break
            even,remaining = k % 2 == 0,v - math.floor(v)
            if even:
                if remaining == 0.5: out += 1
            else:
                if remaining == 0: out += 1
            k += 1
        return out

# Tests.
assert(Solution().consecutiveNumbersSum(5) == 2)
assert(Solution().consecutiveNumbersSum(9) == 3)
assert(Solution().consecutiveNumbersSum(15) == 4)
assert(Solution().consecutiveNumbersSum2(4) == 1)
assert(Solution().consecutiveNumbersSum2(5) == 2)
assert(Solution().consecutiveNumbersSum2(9) == 3)
assert(Solution().consecutiveNumbersSum2(15) == 4)