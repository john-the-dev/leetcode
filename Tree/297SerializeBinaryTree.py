# 297. Serialize and Deserialize Binary Tree
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import *
class Codec:
    '''
    Breath first search to locate nodes in order and put them in result string. Put 'null' for empty left or right unless no value after.
    O(n) runtime both for serilaize and deserialize. O(n) storage for both as well.
    Beat 89% runtime, 63% storage of all Leetcode submissions.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        layer,out = [root],[]
        while layer:
            new_layer = []
            is_all_none = True
            for node in layer:
                if node != None: 
                    is_all_none = False
                    break
            for node in layer:
                if node == None:
                    if not is_all_none: out.append('null')
                else:
                    out.append(str(node.val))
                    new_layer.append(node.left)
                    new_layer.append(node.right)
            layer = new_layer
        while out and out[-1] == 'null':
            out.pop()
        return '[{}]'.format(','.join(out))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i,n = 1,len(data)-1
        root,layer = None,[]
        while i < n:
            if root == None:
                j = data.find(',',i)
                if j == -1: j = n
                root = TreeNode(int(data[i:j]))
                layer.append(root)
                i = j+1
            else:
                new_layer = []
                for node in layer:
                    if i >= n: break
                    j = data.find(',',i)
                    if j == -1: j = n
                    k = data.find(',',j+1)
                    if k == -1: k = n
                    if j > i and data[i:j] != 'null': 
                        node.left = TreeNode(int(data[i:j]))
                        new_layer.append(node.left)
                    if k > j+1 and data[j+1:k] != 'null': 
                        node.right = TreeNode(int(data[j+1:k]))
                        new_layer.append(node.right)
                    i = k+1
                layer = new_layer
        return root

# Tests.
root = TreeNode(1)
root.left,root.right = TreeNode(2),TreeNode(3)
root.right.left,root.right.right = TreeNode(4),TreeNode(5)
codec = Codec()
assert_tree(codec.deserialize(codec.serialize(root)), root)
root.right.left.left,root.right.right.left = TreeNode(6),TreeNode(7)
assert_tree(codec.deserialize(codec.serialize(root)), root)
assert_tree(codec.deserialize(codec.serialize(None)), None)
assert(codec.serialize(codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]')) == '[3,5,1,6,2,0,8,null,null,7,4]')