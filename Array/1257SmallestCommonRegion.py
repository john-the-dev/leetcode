# 1257. Smallest Common Region
'''
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.

 

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
 

Constraints:

2 <= regions.length <= 10^4
region1 != region2
All strings consist of English letters and spaces with at most 20 letters.
'''
from common import *
'''
Reverse tree in which each node stores its parent. Then we can search backward to the root from region1 and region2.
O(N) runtime, O(N) storage, in which N is # of nodes in the tree.
Beat 30% runtime, 5% storage of all Leetcode submissions.
'''
class ReverseTreeNode:
    def __init__(self, v):
        self.v = v
        self.parent = None
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        nodes,node1,node2 = {},None,None
        for i in range(len(regions)):
            for j in range(len(regions[i])):
                v = regions[i][j]
                if v not in nodes: nodes[v] = ReverseTreeNode(v)
                if j == 0:                    
                    parent = nodes[v]
                else:
                    nodes[v].parent = parent
                if v == region1: node1 = nodes[v]
                if v == region2: node2 = nodes[v]
        parents1 = set()
        while node1 != None:
            parents1.add(node1.v)
            node1 = node1.parent
        out = None
        while node2 != None:
            if node2.v in parents1:
                out = node2.v
                break
            node2 = node2.parent
        return out

    '''
    A slightly storage optimized version which uses index instead of the string as value in each reverse tree node.
    No improvement seen from Leetcode submission.
    '''
    def findSmallestRegion2(self, regions: List[List[str]], region1: str, region2: str) -> str:
        nodes,node1,node2 = {},None,None
        for i in range(len(regions)):
            for j in range(len(regions[i])):
                v = regions[i][j]
                if v not in nodes: nodes[v] = ReverseTreeNode((i,j))
                if j == 0:                    
                    parent = nodes[v]
                else:
                    nodes[v].parent = parent
                if v == region1: node1 = nodes[v]
                if v == region2: node2 = nodes[v]
        parents1 = set()
        while node1 != None:
            parents1.add(node1.v)
            node1 = node1.parent
        out = None
        while node2 != None:
            if node2.v in parents1:
                out = regions[node2.v[0]][node2.v[1]]
                break
            node2 = node2.parent
        return out
        
# Tests.
assert(Solution().findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]],"Quebec","New York") == "North America")
assert(Solution().findSmallestRegion2([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]],"Quebec","New York") == "North America")

