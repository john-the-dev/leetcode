# 93. Restore IP Addresses
'''
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

0 <= s.length <= 3000
s consists of digits only.
'''
from common import *
class Solution:
    '''
    DFS, return early when not valid.
    O(3^4) runtime, O(4) storage.
    Beat 99.8% runtime, 100% storage of all Leetcode submissions.
    '''
    def restoreIpAddresses(self, s: str) -> List[str]:
        n,out = len(s),[]
        def isValidNumber(i,j):
            if j-i > 3: return False
            if j-i > 1 and s[i] == '0': return False
            num = int(s[i:j])
            if num >= 256: return False
            return True
        def dfs(prefix,i):
            nonlocal out
            k = len(prefix)
            if i >= n: return
            if k == 3:
                if not isValidNumber(i,n): return
                prefix.append(s[i:n])
                out.append('.'.join(prefix))
                prefix.pop()
            else:
                for j in range(i+1,i+4):
                    if not isValidNumber(i,j): continue
                    prefix.append(s[i:j])
                    dfs(prefix,j)
                    prefix.pop()
        dfs([],0)
        return out

# Tests.
assert(Solution().restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"])
assert(Solution().restoreIpAddresses("0000") == ["0.0.0.0"])
assert(Solution().restoreIpAddresses("1111") == ["1.1.1.1"])
assert(Solution().restoreIpAddresses("010010") == ["0.10.0.10","0.100.1.0"])
assert(Solution().restoreIpAddresses("101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])
            

