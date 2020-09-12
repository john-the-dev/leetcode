# 1249. Minimum Remove to Make Valid Parentheses
'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
'''
class Solution:
    '''
    Classic stack approach. Push to stack when encounter '(' or ')' but no matching '(' in stack. Pop from stack when there is matching '(' in stack for current ')'. 
    O(n) runtime, O(m) storage in which m is # of parentheses.
    Beat 45% runtime, 38% storage of all Leetcode submissions.
    '''
    def minRemoveToMakeValid(self, s):
        stack = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append([c,i])
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([c,i])
        out,stack = [],stack[::-1]
        for i,c in enumerate(s):
            if stack and stack[-1][1] == i:
                stack.pop()
            else:
                out.append(c)
        return ''.join(out)

# Tests.
assert(Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de")
assert(Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d")
assert(Solution().minRemoveToMakeValid("))((") == "")
assert(Solution().minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)")