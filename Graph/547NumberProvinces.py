# 547. Number of Provinces
'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''
from common import *
'''
Disjoint set membership.
O(n^3) runtime, O(n) storage.
Beat 35% runtime, 52% storage of all Leetcode submissions.
'''
class DST:
    def __init__(self):
        self.groups = {}
    def find(self, id):
        if id not in self.groups: self.groups[id] = id
        if self.groups[id] != id: self.groups[id] = self.find(self.groups[id])
        return self.groups[id]
    def union(self, id1, id2):
        self.groups[self.find(id1)] = self.find(id2)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n,dst = len(M),DST()
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j] == 1: dst.union(i,j)
        out = set()
        for i in range(n):
            out.add(dst.find(i))
        return len(out)

    '''
    BFS to explore cities within 1 province for each breath iteration.
    O(n^2) runtime, O(n) storage.
    Beat 92% runtime, 89% storage of all Leetcode submissions.
    '''
    def findCircleNum2(self, M: List[List[int]]) -> int:
        seen,count,n = set(),0,len(M)
        for i in range(n):
            if i not in seen:
                seen.add(i)
                count += 1
                layer = [i]
                while layer:
                    new_layer = []
                    for j in layer:
                        for k in range(n):
                            if M[j][k] == 1 and k not in seen:
                                seen.add(k)
                                new_layer.append(k)
                    layer = new_layer
        return count
                


# Tests.
assert(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2)
assert(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3)
assert(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]) == 1)
assert(Solution().findCircleNum([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]) == 8)
assert(Solution().findCircleNum2([[1,1,0],[1,1,0],[0,0,1]]) == 2)
assert(Solution().findCircleNum2([[1,0,0],[0,1,0],[0,0,1]]) == 3)
assert(Solution().findCircleNum2([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]) == 1)
assert(Solution().findCircleNum2([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]) == 8)


            
