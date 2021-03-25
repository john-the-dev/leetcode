# 140. Word Break II
'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    DFS + backtrack + cache + hashmap
    O(2^n) runtime, O(2^n) storage.
    Beat 93% runtime, 63% storage of all Leetcode submissions.
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words,h = set(wordDict),defaultdict(list)
        def dfs(s):
            nonlocal h
            if s == "": return [[]]
            if s in h: return h[s]
            out = []
            for i in range(1,len(s)+1):
                w = s[:i]
                if w in words:
                    for sub in dfs(s[i:]):
                        out.append([w]+sub)
            h[s] = out
            return out
        out = dfs(s)
        return [' '.join(row) for row in out]

# Tests.
assert_list_noorder(Solution().wordBreak("cats", ["cat","cats","and","sand","dog"]), ["cats"])
assert_list_noorder(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog","cats and dog"])
assert_list_noorder(Solution().wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), ["pine apple pen apple","pineapple pen apple","pine applepen apple"])
assert_list_noorder(Solution().wordBreak("catsandog", wordDict = ["cats","dog","sand","and","cat"]), [])