# 49. Group Anagrams
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''
class Solution:
    '''
    Letter count as signature.
    O(n) runtime, O(m) storage, in which n is # of strings and m is # of groups.
    Beat 38% runtime, 43% storage of all Leetcode submissions.
    '''
    def groupAnagrams(self, strs):
        h = {}
        def getAnaSig(s):
            sig,b = [0]*26,ord('a')
            for c in s:
                sig[ord(c)-b] += 1
            return str(sig)
        for s in strs:
            sig = getAnaSig(s)
            if sig not in h: h[sig] = []
            h[sig].append(s)
        return list(h.values())

# Tests.
assert(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
assert(Solution().groupAnagrams([""]) == [[""]])
assert(Solution().groupAnagrams(["a"]) == [["a"]])
assert(Solution().groupAnagrams(["aab","aba","ab","bba"]) == [["aab","aba"],["ab"],["bba"]])