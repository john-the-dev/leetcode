# 22. Generate Parentheses
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from common import *
class Solution:
    '''
    Unwrapped recursion, build the output of func(n) based on func(n-1).
    O(2^n) runtime, O(2^n) storage.
    Beat 58% runtime, 32% storage of all Leetcode submissions.
    Note we can also do recursion, but recursion will use additional memory for recursive calls. So wrapped recursion could save these memory usage. Also use set to make sure no duplicate is generated without increasing runtime complexity.
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        out = set(['()'])
        while n > 1:
            new_out = set()
            for row in out:
                new_out.add('(){}'.format(row))
                cnt = 0
                for i in range(len(row)):
                    cnt = cnt+1 if row[i] == '(' else cnt-1
                    if cnt == 0:
                        left,right = row[:i+1],row[i+1:]
                        new_out.add('({}){}'.format(left,right))
                        new_out.add('{}({})'.format(left,right))
            out,n = new_out,n-1
        return list(out)

# Tests.
assert_list_noorder(Solution().generateParenthesis(1),['()'])
assert_list_noorder(Solution().generateParenthesis(2),['(())', '()()'])
assert_list_noorder(Solution().generateParenthesis(3),['((()))','(()())','(())()','()()()','()(())'])
assert_list_noorder(Solution().generateParenthesis(4),["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
