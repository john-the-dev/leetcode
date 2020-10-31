# 208. Implement Trie (Prefix Tree)
'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''
from common import *
'''
Based on tree.
O(n) runtime for insert, search, and startsWith, in which n is the size of the word, O(n) storage for insert, O(1) storage for search and startsWith.
Beat 70% runtime, 6% storage of all Leetcode submissions.
'''
class Node:
    def __init__(self, v):
        self.v = v
        self.children = {}
        self.done = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = Node(c)
            node = node.children[c]
        node.done = True

    def loc(self, word: str) -> Node:
        node = self.root
        for c in word:
            if c not in node.children: return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.loc(word)
        return node.done if node != None else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.loc(prefix)
        return node != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Tests.
assert_call_sequence(globals(),["Trie","insert","search","search","startsWith","insert","search"],[[],["apple"],["apple"],["app"],["app"],["app"],["app"]],[[None,None,True,False,True,None,True]])