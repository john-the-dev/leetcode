# 974. Subarray Sums Divisible by K
'''
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    Hash map to count # of occurance of same modulo as same modulo indicates subarray is divisible by K.
    O(n) runtime, O(min(n,K)) storage.
    Beat 91% runtime, 24% storage of all Leetcode submissions.
    '''
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        h,total,out = defaultdict(int),0,0
        h[0] = 1
        for v in A:
            total += v
            h[total % K] += 1
        for r in h:
            if h[r] > 1: out += h[r]*(h[r]-1) // 2
        return out

# Tests.
assert(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5) == 7)
assert(Solution().subarraysDivByK([4,5], 5) == 1)
assert(Solution().subarraysDivByK([5,15], 5) == 3)

