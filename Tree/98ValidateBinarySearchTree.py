# 98. Validate Binary Search Tree
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common import *
class Solution:
    '''
    helper with min and max boundary.
    O(n) runtime, O(log(n)) storage for call stack.
    Beat 88% runtime, 54% storage of all Leetcode submissions.
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        def checkValid(node, min, max):
            if node.val <= min or node.val >= max: return False
            if node.left != None:
                if not checkValid(node.left, min, node.val): return False
            if node.right != None:
                if not checkValid(node.right, node.val, max): return False
            return True
        return True if root == None else checkValid(root, float('-inf'), float('inf'))

# Tests.
assert(Solution().isValidBST(Codec().deserialize('[2,1,3]')) == True)
assert(Solution().isValidBST(Codec().deserialize('[5,1,4,null,null,3,6]')) == False)
assert(Solution().isValidBST(Codec().deserialize('[5,4,6,null,null,3,7]')) == False)
        