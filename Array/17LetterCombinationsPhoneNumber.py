# 17. Letter Combinations of a Phone Number
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
from common import *
class Solution:
    '''
    DFS + prefix for output all possible combinations.
    O(3^n) runtime, O(n) storage for call stack and prefix.
    Beat 60% runtime, 35% storage of all Leetcode submissions.
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        n,out = len(digits),[]
        if n == 0: return []
        def dfs(prefix, i):
            nonlocal out
            if i == n:
                out.append(''.join(prefix))
                return
            for c in map[digits[i]]:
                prefix.append(c)
                dfs(prefix,i+1)
                prefix.pop()
        dfs([],0)
        return out

# Tests.
assert_list_noorder(Solution().letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
assert_list_noorder(Solution().letterCombinations("2"), ["a","b","c"])
assert_list_noorder(Solution().letterCombinations(""), [])