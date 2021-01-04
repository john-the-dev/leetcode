# 7. Reverse Integer
'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
'''
from common import *
class Solution:
    '''
    Reverse with string. Check boundary.
    O(n) runtime, O(n) storage, in which n is number of digits in the number.
    Beat 66% runtime, 66% storage of all Leetcode submissions.
    '''
    def reverse(self, x: int) -> int:
        low,high,neg = -2**31,2**31-1,False
        if x < 0: x,neg = -x,True
        out = int(str(x)[::-1])
        if neg: out = -out
        return 0 if out < low or out > high else out

# Tests.
assert(Solution().reverse(123) == 321)
assert(Solution().reverse(-123) == -321)
assert(Solution().reverse(120) == 21)
assert(Solution().reverse(0) == 0)
