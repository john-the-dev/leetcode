# 67. Add Binary
'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
    '''
    Backward add, default to 0 if over length.
    O(max(m,n)) runtime, O(1) storage.
    Beat 91% runtime, 25% storage of all Leetcode submissions.
    '''
    def addBinary(self, a: str, b: str) -> str:
        out,m,n,carry = [],len(a),len(b),0
        for i in range(max(m,n)):
            i1,i2 = m-i-1,n-i-1
            v1 = 0 if i1 < 0 else int(a[i1])
            v2 = 0 if i2 < 0 else int(b[i2])
            v = v1+v2+carry
            if v >= 2:
                v,carry = v-2,1
            else:
                carry = 0
            out.append(str(v))
        if carry > 0: out.append(str(carry))
        return ''.join(out[::-1])

# Tests.
assert(Solution().addBinary(a = "11", b = "1") == "100")
assert(Solution().addBinary(a = "1010", b = "1011") == "10101")
