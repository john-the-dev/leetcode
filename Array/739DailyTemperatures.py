# 739. Daily Temperatures
'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''
from common import *
import sys
from collections import defaultdict
class Solution:
    '''
    Memorization while looping.
    O(n^2) runtime, O(n) storage.
    Beat 5% runtime, 5% storage of all Leetcode submissions.
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        h,out = defaultdict(set),[0]*n
        for i,t in enumerate(T):
            for j in h[t]:
                if out[j] == 0: out[j] = i-j
            h[t].clear()
            for k in range(t+1,101):
                h[k].add(i)
        return out

    '''
    Backward scan + hashmap to remember last seen index + temprature scan (for constant time).
    O(n) runtime, O(n) storage.
    Beat 5% runtime, 74% storage of all Leetcode submissions.
    '''
    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        n = len(T)
        seen,out = {},[0]*n
        for i in range(n-1,-1,-1):
            d = sys.maxsize
            for t in range(T[i]+1,101):
                if t in seen:
                    d = min(seen[t]-i,d)
            if d != sys.maxsize: out[i] = d
            seen[T[i]] = i
        return out

# Tests.
assert(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0])
assert(Solution().dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0])