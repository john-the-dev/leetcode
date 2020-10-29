# 165. Compare Version Numbers
'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
Example 4:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 5:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
'''
from common import *
class Solution:
    '''
    Scan both version strings, parse version numbers for each section and compare accordingly.
    O(max(n1,n2)) runtime, O(1) storage.
    Beat 71% runtime, 99.9% storage of all Leetcode submissions.
    '''
    def compareVersion(self, version1: str, version2: str) -> int:
        i1,i2,n1,n2 = 0,0,len(version1),len(version2)
        while i1 < n1 or i2 < n2:
            if i1 == n1:
                k1,val1 = -1,0
            else:
                k1 = version1.find('.',i1)
                val1 = int(version1[i1:k1]) if k1 > 0 else int(version1[i1:])
            if i2 == n2:
                k2,val2 = -1,0
            else:
                k2 = version2.find('.',i2)
                val2 = int(version2[i2:k2]) if k2 > 0 else int(version2[i2:])
            if val1 < val2: 
                return -1
            elif val1 > val2:
                return 1
            i1 = k1+1 if k1 > 0 else n1
            i2 = k2+1 if k2 > 0 else n2
        return 0

# Tests.
assert(Solution().compareVersion("1.01", "1.001") == 0)
assert(Solution().compareVersion("1.0", "1.0.0") == 0)
assert(Solution().compareVersion("0.1", "1.1") == -1)
assert(Solution().compareVersion("1.0.1", "1") == 1)
assert(Solution().compareVersion("7.5.2.4", "7.5.3") == -1)