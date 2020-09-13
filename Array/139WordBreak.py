# 139. Word Break
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.done = False 
class Solution:
    '''
    Reversed trie with dynamic programming.
    O(n^2) runtime, O(m+n) storage in which m is # of characters in wordDict and n is length of string s.
    Beat 99.7% runtime, 5% storage of all Leetcode submissions.
    '''
    def wordBreak(self, s, wordDict):
        trie,n = TrieNode(),len(s)
        for w in wordDict:
            node = trie
            for i in range(len(w)-1,-1,-1):
                c = w[i]
                if c not in node.children: node.children[c] = TrieNode()
                node = node.children[c]
            node.done = True
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            node,j = trie,i-1
            while j >= 0 and s[j] in node.children:
                node = node.children[s[j]]
                if node.done and dp[j]:
                    dp[i] = True
                    break
                j -= 1
        return dp[n]

assert(Solution().wordBreak("leetcode", ["leet", "code"]) == True)
assert(Solution().wordBreak("applepenapple", ["apple", "pen"]) == True)
assert(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)
assert(Solution().wordBreak("", ["leet", "code"]) == True)
assert(Solution().wordBreak("code", ["leet", "code"]) == True)