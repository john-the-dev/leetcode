# 14. Longest Common Prefix
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    '''
    Horizontal scan of strings.
    O(N) runtime, O(1) storage, in which N is total # of characters.
    Beat 93% runtime, 5% storage of all Leetcode submissions. The storage part of Leetcode is confusing as there is not much storage being used here while it is only 5%.
    '''
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        i = 0
        while True:
            c,match = None,True
            for s in strs:
                if i >= len(s): 
                    match = False
                    break
                if c == None:
                    c = s[i]
                elif c != s[i]:
                    match = False
                    break
            if not match: break
            i += 1
        return strs[0][:i]

# Tests.
assert(Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl")
assert(Solution().longestCommonPrefix(["dog","racecar","car"]) == "")
assert(Solution().longestCommonPrefix(["","flow","flight"]) == "")
assert(Solution().longestCommonPrefix(["flower","flow",""]) == "")
assert(Solution().longestCommonPrefix([]) == "")