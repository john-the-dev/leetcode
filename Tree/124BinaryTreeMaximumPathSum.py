# 124. Binary Tree Maximum Path Sum
'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common import *
import sys
class Solution:
    '''
    Helper function for recursion and global variable for tracking output.
    O(n) runtime, O(d) storage, in which n is # of nodes in the tree and d is the depth of the tree.
    Beat 42% runtime, 26% storage of all Leetcode submissions.
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        out = -sys.maxsize-1
        # This method returns max sum ending with the root.
        def maxSum2Root(root):
            nonlocal out
            left_sum = maxSum2Root(root.left) if root.left != None else 0
            right_sum = maxSum2Root(root.right) if root.right != None else 0
            if root.left != None: out = max(out,left_sum)
            if root.right != None: out = max(out,right_sum)
            out = max(out,left_sum+root.val,right_sum+root.val,left_sum+root.val+right_sum,root.val)
            return max(left_sum+root.val,right_sum+root.val,root.val)
        maxSum2Root(root)
        return out

# Tests.
assert(Solution().maxPathSum(Codec().deserialize('[1,2,3]')) == 6)
assert(Solution().maxPathSum(Codec().deserialize('[-10,9,20,null,null,15,7]')) == 42)
assert(Solution().maxPathSum(Codec().deserialize('[10,11,20,null,null,15,7]')) == 56)
assert(Solution().maxPathSum(Codec().deserialize('[-1]')) == -1)
assert(Solution().maxPathSum(Codec().deserialize('[2,-1,-2]')) == 2)
        
