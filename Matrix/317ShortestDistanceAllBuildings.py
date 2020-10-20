# 317. Shortest Distance from All Buildings
'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''
from common import *
import sys
class Solution:
    '''
    Breath first search from each building to find update distances from each empty space to the building. Then we just need to find the smallest distance on empty space with all buildings having a distance to it.
    O(kmn) runtime, O(mn) storage.
    Beat 64% runtime, 7% storage of all Leetcode submissions.
    '''
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d,buildings = [[[0,0] for j in range(n)] for i in range(m)],0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    distance = 0
                    buildings += 1
                    layer,seen = [(i,j)],set([(i,j)])
                    while layer:
                        new_layer = []
                        for i1,j1 in layer:
                            if distance > 0: 
                                d[i1][j1][0] += distance
                                d[i1][j1][1] += 1
                            if i1 > 0 and grid[i1-1][j1] == 0 and (i1-1,j1) not in seen:
                                new_layer.append((i1-1,j1))
                                seen.add((i1-1,j1))
                            if i1 < m-1 and grid[i1+1][j1] == 0 and (i1+1,j1) not in seen:
                                new_layer.append((i1+1,j1))
                                seen.add((i1+1,j1))
                            if j1 > 0 and grid[i1][j1-1] == 0 and (i1,j1-1) not in seen:
                                new_layer.append((i1,j1-1))
                                seen.add((i1,j1-1))
                            if j1 < n-1 and grid[i1][j1+1] == 0 and (i1,j1+1) not in seen:
                                new_layer.append((i1,j1+1))
                                seen.add((i1,j1+1))
                        layer,distance = new_layer,distance+1
        out = sys.maxsize
        for i in range(m):
            for j in range(n):
                if d[i][j][1] == buildings and grid[i][j] == 0:
                    out = min(out,d[i][j][0])
        return out if out < sys.maxsize else -1

assert(Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]) == 7)
assert(Solution().shortestDistance([[1,2,2,0,1],[2,0,0,0,0],[0,0,1,0,0]]) == -1) # 1 building is blocked.
                    


