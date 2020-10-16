# 864. Shortest Path to Get All Keys
'''
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

 

Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6
 

Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
'''
from common import *
import sys
import heapq
class Solution:
    '''
    Dijkstra's algorithm.
    O(64m^2n^2log(64mn)) runtime, O(64mn) storage.
    Beat 57% runtime, 5% storage of all Leetcode submissions.
    Note we need to save the shortest path (cost) for every key combination status.
    '''
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m,n = len(grid),len(grid[0])
        visits,costs,stop_status = [],[[[sys.maxsize for k in range(2**6+1)] for j in range(n)] for i in range(m)],0
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start = (i,j)
                elif c >= 'a' and c <= 'f':
                    stop_status = stop_status | 2**(ord(c)-ord('a'))
        costs[start[0]][start[1]][0] = 0
        visits.append((0,0,start))
        while visits:
            cost,status,loc = heapq.heappop(visits)
            if status == stop_status: return cost
            locs = []
            if loc[0] > 0: locs.append((loc[0]-1,loc[1]))
            if loc[0] < m-1: locs.append((loc[0]+1,loc[1]))
            if loc[1] > 0: locs.append((loc[0],loc[1]-1))
            if loc[1] < n-1: locs.append((loc[0],loc[1]+1))
            for i,j in locs:
                c = grid[i][j]
                if c == '#': continue
                if c >= 'a' and c <= 'f':
                    new_status = status | 2**(ord(c)-ord('a'))
                    if cost+1 < costs[i][j][new_status]:
                        costs[i][j][new_status] = cost+1
                        heapq.heappush(visits, (cost+1,new_status,(i,j)))
                elif c >= 'A' and c <= 'F':
                    if status & 2**(ord(c.lower())-ord('a')):
                        if cost+1 < costs[i][j][status]:
                            costs[i][j][status] = cost+1
                            heapq.heappush(visits, (cost+1,status,(i,j)))
                elif c == '.' or c == '@':
                    if cost+1 < costs[i][j][status]:
                        costs[i][j][status] = cost+1
                        heapq.heappush(visits, (cost+1,status,(i,j)))
        return -1

# Tests.
assert(Solution().shortestPathAllKeys(["@.a.#","###.#","b.A.B"]) == 8)
assert(Solution().shortestPathAllKeys(["@..aA","..B#.","....b"]) == 6)
assert(Solution().shortestPathAllKeys(["@...a",".###A","b.BCc"]) == 10)