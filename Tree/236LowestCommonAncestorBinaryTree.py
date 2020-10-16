# 236. Lowest Common Ancestor of a Binary Tree
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import *
class Solution:
    '''
    Recursion + global variable (ancestor). Through pre order traverse recursion to locate the node which contains p and q as child node or itself. Assign the first such node to ancestor.
    O(n) runtime, O(log(n)) storage.
    Beat 80% runtime, 5% storage of all Leetcode submissions. The low storage should be due to returning a pair of values, which does not change the complexity.
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc = None
        def find(node):
            nonlocal anc
            p_found = (node.val == p.val)
            q_found = (node.val == q.val)
            if node.left != None:
                found = find(node.left)
                p_found = p_found or found[0]
                q_found = q_found or found[1]
            if node.right != None:
                found = find(node.right)
                p_found = p_found or found[0]
                q_found = q_found or found[1]
            if p_found and q_found and anc == None: anc = node
            return [p_found,q_found]
        if root != None: find(root)
        return anc

# Tests.
codec = Codec()
assert(Solution().lowestCommonAncestor(codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(1)).val == 3)
assert(Solution().lowestCommonAncestor(codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(4)).val == 5)
assert(Solution().lowestCommonAncestor(codec.deserialize('[1,2]'), TreeNode(1), TreeNode(2)).val == 1)