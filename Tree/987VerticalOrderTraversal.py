# 987. Vertical Order Traversal of a Binary Tree
'''
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
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
    Breath first search to keep output append in order.
    O(nlog(n/k)) runtime, O(n) storage, in which n is # of nodes and k is # of verticals.
    How runtime complexity is calculated? It is a upper bound.
    '''
    def verticalTraversal(self, root):
        if root == None: return []
        left,right = 0,0
        def boundary(node, x):
            nonlocal left, right
            left = min(left, x)
            right = max(right, x)
            if node.left != None: boundary(node.left, x-1)
            if node.right != None: boundary(node.right, x+1)
        boundary(root, 0)
        n = right - left + 1
        out = [[] for i in range(n)]
        layer = {0: [root]}
        while layer:
            new_layer = {}
            for i in layer:
                nodes = layer[i]
                nodes.sort(key = lambda row: row.val)
                for node in nodes:
                    out[i-left].append(node.val)
                    if node.left != None:
                        if i-1 not in new_layer: new_layer[i-1] = []
                        new_layer[i-1].append(node.left)
                    if node.right != None:
                        if i+1 not in new_layer: new_layer[i+1] = []
                        new_layer[i+1].append(node.right)
            layer = new_layer
        return out

    '''
    Recursion to mark node. init x,y, and then dec or inc 1, record min and max, hash map to allow for retrieve value based on x and y with O(1).
    O(nlog(n/k)) runtime, O(n) storage.
    '''
    def verticalTraversal2(self, root):
        if root == None: return []
        h,minx,maxx,miny,maxy = {},0,0,0,0
        def markNode(root,x,y):
            nonlocal minx,maxx,miny,maxy
            if root == None: return
            if x not in h: h[x] = {}
            if y not in h[x]: h[x][y] = []
            h[x][y].append(root.val)
            minx,maxx = min(x,minx),max(x,maxx)
            miny,maxy = min(y,miny),max(y,maxy)
            markNode(root.left,x-1,y+1)
            markNode(root.right,x+1,y+1)
        markNode(root,0,0)
        out = []
        for i in range(minx,maxx+1):
            out.append([])
            for j in range(miny,maxy+1):
                if i not in h: continue
                if j in h[i]:
                    r = h[i][j]
                    if len(r) > 1: r.sort()
                    out[-1].extend(r)
        return out

# Tests.
assert(Solution().verticalTraversal(Codec().deserialize('[3,9,20,null,null,15,7]')) == [[9],[3,15],[20],[7]])
assert(Solution().verticalTraversal(Codec().deserialize('[1,2,3,4,5,6,7]')) == [[4],[2],[1,5,6],[3],[7]])
assert(Solution().verticalTraversal(Codec().deserialize('[]')) == [])
assert(Solution().verticalTraversal(Codec().deserialize('[0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]')) == [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]])
assert(Solution().verticalTraversal(Codec().deserialize('[0,1,2,4,5,9,3,11,null,null,10,15,null,6,18,14,null,null,21,null,null,7,12,null,null,22,null,null,24,13,8,null,17,null,null,null,null,null,null,16,19,null,null,null,null,23,20]')) == [[22],[14],[11],[4],[1,15,13],[0,5,9,7,16],[2,6,10,8,23],[3,12,21,19],[18,17,24,20]])
assert(Solution().verticalTraversal2(Codec().deserialize('[3,9,20,null,null,15,7]')) == [[9],[3,15],[20],[7]])
assert(Solution().verticalTraversal2(Codec().deserialize('[1,2,3,4,5,6,7]')) == [[4],[2],[1,5,6],[3],[7]])
assert(Solution().verticalTraversal2(Codec().deserialize('[]')) == [])
assert(Solution().verticalTraversal2(Codec().deserialize('[0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]')) == [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]])
assert(Solution().verticalTraversal2(Codec().deserialize('[0,1,2,4,5,9,3,11,null,null,10,15,null,6,18,14,null,null,21,null,null,7,12,null,null,22,null,null,24,13,8,null,17,null,null,null,null,null,null,16,19,null,null,null,null,23,20]')) == [[22],[14],[11],[4],[1,15,13],[0,5,9,7,16],[2,6,10,8,23],[3,12,21,19],[18,17,24,20]])