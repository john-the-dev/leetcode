# 336. Palindrome Pairs
'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i] <= 300
words[i] consists of lower-case English letters.
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    Create a list of prefixes and surfixes and check if each word is in the lists.
    O(nm^2) runtime, O(nm^2) storage.
    Beat 65% runtime, 17% storage of all Leetcode submissions.
    '''
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        fronts = defaultdict(list)
        rears = defaultdict(list)
        def isSubPalindrome(w,i,j):
            while i < j:
                if w[i] != w[j]: return False
                i += 1
                j -= 1
            return True
        for i,w in enumerate(words):
            fronts[w[::-1]].append(i)
            rears[w[::-1]].append(i)
            m = len(w)
            j,k = m-1,m-1
            while j >= 0:
                if isSubPalindrome(w,j,k): fronts[w[:j][::-1]].append(i)
                j -= 1
            j,k = 0,0
            while k < m:
                if isSubPalindrome(w,j,k): rears[w[k+1:][::-1]].append(i)
                k += 1
        out = set()
        for i,w in enumerate(words):
            for j in fronts[w]:
                if i != j: out.add((j,i))
            for j in rears[w]:
                if i != j: out.add((i,j))
        return [list(p) for p in list(out)]

# Tests.
assert_list_noorder(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]),[[0,1],[1,0],[3,2],[2,4]])
assert_list_noorder(Solution().palindromePairs(["bat","tab","cat"]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs(["a",""]),[[0,1],[1,0]])
