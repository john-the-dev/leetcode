# 91. Decode Ways
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''
from common import *
class Solution:
    '''
    Dynamic programming, dp[i] can be constrcuted from dp[i-1], dp[i-2].
    O(n) runtime, O(n) storage.
    Beat 68% runtime, 5% storage of all Leetcode submissions.
    Note if all combinations need to be output, then dp cannot work as the dp array only store numbers.
    '''
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0],dp[1] = 1,1 if s[0] != '0' else 0
        for i in range(1,n):
            if s[i] != '0': dp[i+1] += dp[i]
            if s[i-1] == '0': continue
            v = int(s[i-1:i+1])
            if v > 0 and v <= 26: dp[i+1] += dp[i-1]
        return dp[n]

# Tests.
assert(Solution().numDecodings("12") == 2)
assert(Solution().numDecodings("226") == 3)
assert(Solution().numDecodings("0") == 0)
assert(Solution().numDecodings("1") == 1)
assert(Solution().numDecodings("227") == 2)
assert(Solution().numDecodings("2101") == 1)