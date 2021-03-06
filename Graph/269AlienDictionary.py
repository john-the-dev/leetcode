# 269. Alien Dictionary
'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    Graph topological sort.
    O(V+E) runtime, O(V+E) storage.
    Beat 58% runtime, 100% storage of all Leetcode submissions.
    '''
    def alienOrder(self, words: List[str]) -> str:
        graph,visits = defaultdict(set),{}
        for i in range(len(words)-1):
            for c in words[i]:
                visits[c] = -1
            done = False
            for j in range(min(len(words[i]),len(words[i+1]))):
                if words[i][j] != words[i+1][j]: 
                    graph[words[i][j]].add(words[i+1][j])
                    done = True
                    break
            if not done and len(words[i]) > len(words[i+1]): return ''
        for c in words[-1]:
            visits[c] = -1
        out = []
        def dfs(c):
            nonlocal out,visits
            if visits[c] == 0: return False
            if visits[c] == 1: return True
            visits[c] = 0
            for t in graph[c]:
                if not dfs(t): return False
            out.append(c)
            visits[c] = 1
            return True
        for c in visits:
            if visits[c] == -1:
                if not dfs(c): return ''
        return ''.join(out[::-1])

    '''
    2nd implementation, graph topological sort (graph, coloring, dfs)
    O(V+E) runtime, O(V+E) storage.
    Beat 24% runtime, 79% storage of all Leetcode submissions.
    '''
    def alienOrder2(self, words: List[str]) -> str:
        graph,out = {},[]
        for w in words:
            for c in w:
                if c not in graph: graph[c] = {'val': c, 'visit':-1, 'targets': set()}
        for i in range(1,len(words)):
            w1,w2 = words[i-1],words[i]
            l1,l2 = len(w1),len(w2)
            if l1 > l2 and w1[:l2] == w2: return ""
            for j in range(min(l1,l2)):
                if w2[j] != w1[j]: 
                    graph[w1[j]]['targets'].add(w2[j])
                    break
        def dfs(node):
            nonlocal out
            if node['visit'] == 0: return False
            if node['visit'] == 1: return True
            node['visit'] = 0
            for c in node['targets']:
                if not dfs(graph[c]): return False
            node['visit'] = 1
            out.append(node['val'])
            return True
        for c in graph:
            if not dfs(graph[c]): return ""
        return ''.join(out[::-1])

# Tests.
assert(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf")
assert(Solution().alienOrder(["z","x"]) == "zx")
assert(Solution().alienOrder(["z","x","z"]) == "")
assert(Solution().alienOrder(["za","zb","ca","cb"]) == "abzc")
assert(Solution().alienOrder(["abc","ab"]) == "")  # A letter should not proceed before empty.
assert(Solution().alienOrder2(["wrt","wrf","er","ett","rftt"]) == "wertf")
assert(Solution().alienOrder2(["z","x"]) == "zx")
assert(Solution().alienOrder2(["z","x","z"]) == "")
assert(Solution().alienOrder2(["za","zb","ca","cb"]) in set(["abzc","zcab"]))
assert(Solution().alienOrder2(["abc","ab"]) == "")