# 387. First Unique Character in a String
'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    Hash map to record # of times a character appear. Then find the first one whose count is 1.
    O(n) runtime, O(1) storage (there are constant # of characters).
    Beat 57% runtime, 43% storage of all Leetcode submissions.
    '''
    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(int)
        for c in s:
            h[c] += 1
        for i,c in enumerate(s):
            if h[c] == 1: return i
        return -1

# Tests.
assert(Solution().firstUniqChar("leetcode") == 0)
assert(Solution().firstUniqChar("loveleetcode") == 2)
assert(Solution().firstUniqChar("etet") == -1)
        