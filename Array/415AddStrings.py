# 415. Add Strings
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
from common import *
class Solution:
    '''
    Rule: add from end to begining, handle carry, add leading 0 if not same size.
    O(max(n1,n2)) runtime, O(1) storage (not consider output)
    Beat 84% runtime, 11% storage of all Leetcode submissions.
    '''
    def addStrings(self, num1: str, num2: str) -> str:
        n1,n2 = len(num1),len(num2)
        if n1 < n2: n1,n2,num1,num2 = n2,n1,num2,num1
        i,out,c = 0,[],0
        while i < n1:
            j1,j2 = n1-i-1,n2-i-1
            v1,v2 = int(num1[j1]),int(num2[j2]) if j2 >= 0 else 0
            v = v1+v2+c
            c = v // 10
            out.append(str(v % 10))
            i += 1
        if c > 0: out.append(str(c))
        return ''.join(out[::-1])

# Tests.
assert(Solution().addStrings('1','2') == '3')
assert(Solution().addStrings('0','0') == '0')
assert(Solution().addStrings('1','9') == '10')
assert(Solution().addStrings('19','2') == '21')
assert(Solution().addStrings('12345678213456','37492737482029237463728') == '37492737494374915677184')
