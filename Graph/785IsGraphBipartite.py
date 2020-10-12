# 785. Is Graph Bipartite?
'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
'''
from common import *
class Solution:
    '''
    Coloring with depth first search: color first node as red, then any nodes connecting to it is black, then any nodes connecting to nodes of nodes is red again. 
    O(m) runtime, O(n) storage, in which m is # of edges and n is # of nodes.
    Beat 97% runtime, 19% storage of all Leetcode submissions.
    Note we must do it through dfs. Otherwise, we don't know how to color the initial node.
    '''
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [None]*n
        def dfs(i,color):
            if colors[i] == color: return True
            if colors[i] != None and colors[i] != color: return False
            colors[i] = color
            for j in graph[i]:
                if not dfs(j,-color): return False
            return True
        for i in range(n):
            if colors[i] == None:
                if not dfs(i,1): return False
        return True

# Tests.
assert(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]) == True)
assert(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]) == False)
assert(Solution().isBipartite([[3],[2,4],[1],[0,4],[1,3]]) == True)