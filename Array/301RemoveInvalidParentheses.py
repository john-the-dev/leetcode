# 301. Remove Invalid Parentheses
'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''
from common import *
class Solution:
    '''
    DFS + backtracking of prefix, stack, removals.
    O(2^n) runtime, O(n) storage.
    Beat 5% runtime, 56% storage of all Leetcode submissions.
    '''
    def removeInvalidParentheses(self, s: str) -> List[str]:
        minimum,n,out = float('inf'),len(s),set()
        def dfs(prefix, stack, i, removals, find_minimum):
            nonlocal minimum, out
            if i == n:
                if not stack:
                    if find_minimum:
                        minimum = min(removals, minimum)
                    elif removals == minimum:
                        out.add(''.join(prefix))
                return
            if s[i] == '(':
                prefix.append(s[i])
                stack.append(s[i])
                dfs(prefix, stack, i+1, removals, find_minimum)
                stack.pop()
                prefix.pop()
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    prefix.append(s[i])
                    stack.pop()
                    dfs(prefix, stack, i+1, removals, find_minimum)
                    stack.append('(')
                    prefix.pop()
            else:
                prefix.append(s[i])
                dfs(prefix, stack, i+1, removals, find_minimum)
                prefix.pop()
            dfs(prefix, stack, i+1, removals+1, find_minimum)
        dfs([],[],0,0,True)
        dfs([],[],0,0,False)
        return list(out)

# Tests.
assert_list_noorder(Solution().removeInvalidParentheses("()())()"), ["(())()","()()()"])
assert_list_noorder(Solution().removeInvalidParentheses("(a)())()"), ["(a())()","(a)()()"])
assert_list_noorder(Solution().removeInvalidParentheses(")("), [""])

