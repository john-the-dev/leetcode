# 763. Partition Labels
'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''
from typing import List
class Solution:
    '''
    Hash map to memorize right most location of each character. Then use this information to partition.
    O(n) runtime, O(1) storage (This is because total number of unique characters is 26.)
    Beat 86% runtime, 5% storage of all Leetcode submissions.
    '''
    def partitionLabels(self, S: str) -> List[int]:
        indexes,j,k,out = {},-1,-1,[]
        for i,c in enumerate(S):
            indexes[c] = i
        for i,c in enumerate(S):
            j = max(j,indexes[c])
            if i == j:
                out.append(j-k)
                k = j
        return out

# Tests.
assert(Solution().partitionLabels("ababcbacadefegdehijhklij") == [9,7,8])
assert(Solution().partitionLabels("adefegdehijhklij") == [1,7,8])
assert(Solution().partitionLabels("adefegdej") == [1,7,1])
assert(Solution().partitionLabels("") == [])