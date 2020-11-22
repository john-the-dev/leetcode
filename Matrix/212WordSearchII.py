# 212. Word Search II
'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''
from common import *
class Solution:
    '''
    DFS + Trie. Trie to allow quick search in words from prefix and DFS to allow explore all possible combinations.
    O(mn3^(d-1)) runtime, O(S) storage, in which d is the max size of word in words and S is the total # of characters in words.
    Beat 13% runtime, 74% storage of all Leetcode submissions.
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(None)
        for i,w in enumerate(words):
            node = trie
            for c in w:
                if c not in node.children: node.children[c] = Trie(None)
                node = node.children[c]
            node.val = i
        out,m,n = set(),len(board),len(board[0])
        def dfs(i, j, node, used):
            nonlocal out
            if board[i][j] not in node.children: return
            node = node.children[board[i][j]]
            used.add((i,j))
            if node.val != None: out.add(node.val)
            if i > 0 and (i-1,j) not in used: dfs(i-1,j,node,used)
            if i < m-1 and (i+1,j) not in used: dfs(i+1,j,node,used)
            if j > 0 and (i,j-1) not in used: dfs(i,j-1,node,used)
            if j < n-1 and (i,j+1) not in used: dfs(i,j+1,node,used)
            used.remove((i,j))
        for i in range(m):
            for j in range(n):
                dfs(i,j,trie,set())
        return [words[i] for i in out]

# Tests.
assert_list_noorder(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]),["eat","oath"])
assert_list_noorder(Solution().findWords([["a","b"],["c","d"]], ["abcb"]),[])
assert_list_noorder(Solution().findWords([["a","b"],["c","d"]], ["abdc"]),["abdc"])
            
