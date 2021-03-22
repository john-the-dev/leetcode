# 20. Valid Parentheses
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
from common import *
class Solution:
    '''
    Class stack based solution.
    O(n) runtime, O(n) storage.
    Beat 96% runtime, 38% storage of all Leetcode submissions.
    '''
    def isValid(self, s: str) -> bool:
        stack,open,close = [],{'(':0,'[':1,'{':2},{')':0,']':1,'}':2}
        for c in s:
            if c in open:
                stack.append(c)
            elif not stack or open[stack[-1]] != close[c]:
                return False
            else:
                stack.pop()
        return not stack

# Tests.
assert(Solution().isValid("()") == True)
assert(Solution().isValid("()[]{}") == True)
assert(Solution().isValid("(]") == False)
assert(Solution().isValid("([)]") == False)
assert(Solution().isValid("{[]}") == True)
