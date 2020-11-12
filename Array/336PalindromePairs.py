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

    '''
    Brute force solution.
    O(n^2m) runtime, O(m) storage.
    Time limit exceeded for long input.
    '''
    def palindromePairs2(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        def isPalindrome(w):
            i,j = 0,len(w)-1
            while i < j:
                if w[i] != w[j]: return False
                i += 1
                j -= 1
            return True
        out = []
        for i in range(n):
            for j in range(i+1,n):
                if isPalindrome(words[i]+words[j]): out.append([i,j])
                if isPalindrome(words[j]+words[i]): out.append([j,i])
        return out

    '''
    Further improve storage with Trie.
    O(nm^2) runtime, O(nm^2) storage.
    Beat 5% runtime, 6% storage of all Leetcode submissions. These numbers are not good relection of the improvement.
    Note the palindrome word in Trie should be stored reversed so they share same prefix for source word.
    '''
    def palindromePairs3(self, words: List[str]) -> List[List[int]]:
        fronts,rears = Trie(set()),Trie(set())
        def isSubPalindrome(w,i,j):
            while i < j:
                if w[i] != w[j]: return False
                i += 1
                j -= 1
            return True
        def check(root,w):
            node = root
            for c in w:
                if c not in node.children: return set()
                node = node.children[c]
            return node.v
        def add(root,w,i):
            node = root
            for c in w:
                if c not in node.children: node.children[c] = Trie(set())
                node = node.children[c]
            node.v.add(i)
        for i,w in enumerate(words):
            add(fronts,w,i)
            add(rears,w,i)
            m = len(w)
            j,k = m-1,m-1
            while j >= 0:
                if isSubPalindrome(w,j,k): add(fronts,w[:j],i)
                j -= 1
            j,k = 0,0
            while k < m:
                if isSubPalindrome(w,j,k): add(rears,w[k+1:],i)
                k += 1
        out = set()
        for i,w in enumerate(words):
            for j in check(fronts,w[::-1]):
                if i != j: out.add((j,i))
            for j in check(rears,w[::-1]):
                if i != j: out.add((i,j))
        return [list(p) for p in list(out)]

    '''
    Find list of valid suffix and prefix and check against their reverse.
    O(nm^2) runtime, O(nm+m^2) storage.
    Beat 82% runtime, 5% storage of all Leetcode submissions.
    Note we avoided using set to remove duplicate in results with this approach.
    '''
    def palindromePairs4(self, words: List[str]) -> List[List[int]]:
        h = {w:i for i,w in enumerate(words)}
        def isValidSubPalindrome(w,i,j):
            while i < j:
                if w[i] != w[j]: return False
                i,j = i+1,j-1
            return True
        def findValidSuffixes(w):
            n,out = len(w),[]
            for i in range(n):
                if isValidSubPalindrome(w,0,i): out.append(w[i+1:])
            return out
        def findValidPrefixes(w):
            n,out = len(w),[]
            for i in range(n):
                if isValidSubPalindrome(w,i,n-1): out.append(w[:i])
            return out
        out = []
        for i,w in enumerate(words):
            reversed = w[::-1]
            if reversed in h and h[reversed] != i: out.append([i,h[reversed]])
            for suffix in findValidSuffixes(w):
                reversed = suffix[::-1]
                if reversed in h: out.append([h[reversed],i])
            for prefix in findValidPrefixes(w):
                reversed = prefix[::-1]
                if reversed in h: out.append([i,h[reversed]])
        return out

    '''
    Further improve approach 4 with Trie.
    O(nm^2) runtime, O(nm) storage.
    Beat 8% runtime, 5% storage.
    '''
    def palindromePairs5(self, words: List[str]) -> List[List[int]]:
        root = Trie(None)
        reversed_root = Trie(None)
        for i,w in enumerate(words):
            node = root
            for c in w:
                if c not in node.children: node.children[c] = Trie(None)
                node = node.children[c]
            node.v = i
            node = reversed_root
            for j in range(len(w)-1,-1,-1):
                c = w[j]
                if c not in node.children: node.children[c] = Trie(None)
                node = node.children[c]
            node.v = i
        def isValidSubPalindrome(w,i,j):
            while i < j:
                if w[i] != w[j]: return False
                i,j = i+1,j-1
            return True
        def findValidSuffixes(w):
            n,out = len(w),set()
            for i in range(n):
                if isValidSubPalindrome(w,0,i): out.add(n-i-1)
            return out
        def findValidPrefixes(w):
            n,out = len(w),set()
            for i in range(n):
                if isValidSubPalindrome(w,i,n-1): out.add(i)
            return out
        def lookup(w,root,valid):
            node = root
            out = []
            for i,c in enumerate(w):
                if i in valid and node.v != None: out.append(node.v)
                if c not in node.children: return out
                node = node.children[c]
            if len(w) in valid and node.v != None: out.append(node.v)
            return out
        out = []
        for i,w in enumerate(words):
            reversed,valid = w[::-1],set([len(w)])
            for j in lookup(reversed,root,valid):
                if j != i: out.append([i,j])
            valid = findValidSuffixes(w)
            for j in lookup(reversed,root,valid):
                out.append([j,i])
            valid = findValidPrefixes(w)
            for j in lookup(w,reversed_root,valid):
                out.append([i,j])
        return out

# Tests.
assert_list_noorder(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]),[[0,1],[1,0],[3,2],[2,4]])
assert_list_noorder(Solution().palindromePairs(["bat","tab","cat"]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs(["a",""]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs2(["abcd","dcba","lls","s","sssll"]),[[0,1],[1,0],[3,2],[2,4]])
assert_list_noorder(Solution().palindromePairs2(["bat","tab","cat"]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs2(["a",""]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs3(["abcd","dcba","lls","s","sssll"]),[[0,1],[1,0],[3,2],[2,4]])
assert_list_noorder(Solution().palindromePairs3(["bat","tab","cat"]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs3(["a",""]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs4(["abcd","dcba","lls","s","sssll"]),[[0,1],[1,0],[3,2],[2,4]])
assert_list_noorder(Solution().palindromePairs4(["bat","tab","cat"]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs4(["a",""]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs5(["abcd","dcba","lls","s","sssll"]),[[0,1],[1,0],[3,2],[2,4]])
assert_list_noorder(Solution().palindromePairs5(["bat","tab","cat"]),[[0,1],[1,0]])
assert_list_noorder(Solution().palindromePairs5(["a",""]),[[0,1],[1,0]])
