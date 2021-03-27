# 767. Reorganize String
'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''
from common import *
from collections import defaultdict
import heapq
class Solution:
    '''
    Priority queue to use high frequency characters first.
    O(nlog(a)) runtime, O(a) storage, where n is length of S and a is # of unique characters.
    Beat 73% runtime, 35% storage of all Leetcode submissions.
    '''
    def reorganizeString(self, S: str) -> str:
        h = defaultdict(int)
        for c in S:
            h[c] += 1
        q = []
        for c in h:
            q.append([-h[c],c])
        heapq.heapify(q)
        out = []
        while q:
            f,c = heapq.heappop(q)
            if not out or out[-1] != c:
                out.append(c)
                if f < -1: heapq.heappush(q, [f+1,c])
            else:
                if not q: return ""
                f2,c2 = heapq.heappop(q)
                out.append(c2)
                if f2 < -1: heapq.heappush(q, [f2+1,c2])
                heapq.heappush(q, [f,c])
        return ''.join(out)

# Tests.
assert(Solution().reorganizeString("aab") == "aba")
assert(Solution().reorganizeString("aaab") == "")


                