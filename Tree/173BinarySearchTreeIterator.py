# 173. Binary Search Tree Iterator
'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common import *
class BSTIterator:
    '''
    Stack as the core data structure to memorize the status of iterator (the left most nodes of the tree).
    O(log(n)) runtime for __init__, O(log(n)) worst, O(1) average runtime for next, O(1) runtime for hasNext. O(log(n)) storage.
    Beat 96% runtime, 6% storage of all Leetcode submissions.
    '''
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        """
        root = self.stack.pop()
        out = root.val
        root = root.right
        while root:
            self.stack.append(root)
            root = root.left
        return out

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Tests.
codec = Codec()
assert_call_sequence(globals(), ["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"], [[codec.deserialize('[7,3,15,null,null,9,20]')],[],[],[],[],[],[],[],[],[]], [[None,3,7,True,9,True,15,True,20,False]])
assert_call_sequence(globals(), ["BSTIterator","hasNext"], [[codec.deserialize('[]')],[]], [[None,False]])