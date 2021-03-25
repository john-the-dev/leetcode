# 224. Basic Calculator
'''
Given a string s representing an expression, implement a basic calculator to evaluate it.

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'''
from common import *
class Solution:
    '''
    Stack based, consume immediately when computable.
    O(n) runtime, O(n) storage.
    Beat 5% runtime, 35% storage of all Leetcode submissions.
    '''
    def calculate(self, s: str) -> int:
        i,n,stack,ops,pa = 0,len(s),[],{'+':1,'-':2},{'(':1,')':2}
        def getItem(i):
            type,v = 0,0
            while i < n and s[i] == ' ': i += 1
            while i < n and s[i].isdigit():
                type = 1
                v = v*10 + int(s[i])
                i += 1
            if type == 0 and i < n and s[i] in ops:
                type = 2
                v = ops[s[i]]
                i += 1
            if type == 0 and i < n and s[i] in pa:
                type = 3
                v = pa[s[i]]
                i += 1
            return [type,v,i]
        
        while i<n:
            type,v,i = getItem(i)
            if type == 1:
                stack.append([type,v])
            elif type == 2:
                stack.append([type,v])
            elif type == 3:
                if v == 1:
                    stack.append([type,v])
                else:
                    stack[-2] = stack[-1]
                    stack.pop()
            if len(stack) >= 2 and stack[-2][0] == 2 and (len(stack) == 2 or stack[-3][0] != 1) and stack[-1][0] == 1: # Handle negative number
                if stack[-2][1] == 2: stack[-1][1] = -stack[-1][1] 
                stack[-2] = stack[-1]
                stack.pop()
            if len(stack) >= 3 and stack[-2][0] == 2 and stack[-1][0] == 1:
                stack[-3][1] = stack[-3][1]+stack[-1][1] if stack[-2][1] == 1 else stack[-3][1]-stack[-1][1]
                stack.pop()
                stack.pop()
        return stack[-1][1]

# Tests.
assert(Solution().calculate("1 + 1") == 2)
assert(Solution().calculate(" 2-1 + 2 ") == 3)
assert(Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23)
assert(Solution().calculate("-2+ 1") == -1)
assert(Solution().calculate("- (3 + (4 + 5))") == -12)
assert(Solution().calculate("1-(+1+1)") == -1)


            