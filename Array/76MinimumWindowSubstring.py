# 76. Minimum Window Substring
'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?
'''
from common import *
import sys
class Solution:
    '''
    letter count table as signature, special compare, sliding window.
    O(m+n) runtime, O(1) storage.
    Beat 5% runtime, 16% storage of all Leetcode submissions.
    '''
    def minWindow(self, s: str, t: str) -> str:
        sigT,sigS,b = [0]*58,[0]*58,ord('A')
        for c in t:
            sigT[ord(c)-b] += 1
        def compareSig(sigS, sigT):
            for i in range(len(sigT)):
                if sigS[i] < sigT[i]: return -1
            for i in range(len(sigT)):
                if sigT[i] > 0 and sigS[i] > sigT[i]: return 1
            return 0
        i,j,n,out = 0,0,len(s),[0,sys.maxsize]
        while j < n:
            while j < n:
                sigS[ord(s[j])-b] += 1
                j += 1
                if compareSig(sigS,sigT) >= 0: break
            while i < j and compareSig(sigS,sigT) >= 0:
                if j-i < out[1]-out[0]: out = [i,j]
                sigS[ord(s[i])-b] -= 1
                i += 1
        return s[out[0]:out[1]] if out[1] != sys.maxsize else ""

# Tests.
assert(Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC")
assert(Solution().minWindow("a", "a") == "a")
assert(Solution().minWindow("a", "aa") == "")
            
            