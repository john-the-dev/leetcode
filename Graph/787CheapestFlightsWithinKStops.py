# 787. Cheapest Flights Within K Stops
'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''
from common import *
from collections import defaultdict
import sys
import heapq
class Solution:
    '''
    DFS.
    Time limit exceeded for large flights and big K because the runtime is O(V^K).
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        h,visited = defaultdict(list),set()
        for s,d,p in flights:
            h[s].append([d,p])
        def dfs(i,step):
            if i in visited: return -1
            if step > K: return -1
            if i == dst: return 0
            visited.add(i)
            cost = -1
            for flight in h[i]:
                cost1 = dfs(flight[0],step+1)
                if cost1 == -1: continue
                cost = cost1+flight[1] if cost == -1 else min(cost,cost1+flight[1])
            visited.remove(i)
            return cost
        out = dfs(src,-1)
        return out
    
    '''
    Dijkstra's algorithm.
    O(V^2Klog(VK)) runtime, O(V^2+VK) storage.
    Beat 99% runtime, 6% storage of all Leetcode submissions.
    Note in order to deal with the constraint on K stops, we have to keep track of the cheapest price for all stops.
    '''
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        h,visits,costs = defaultdict(list),[],[[sys.maxsize for j in range(K+1)] for i in range(n)]
        visits.append((0,-1,src))
        for s,d,p in flights:
            h[s].append([d,p])
        while visits:
            cost,stops,s = heapq.heappop(visits)
            if s == dst: return cost
            if stops+1 > K: continue
            for d,p in h[s]:
                if cost+p < costs[d][stops+1]:
                    costs[d][stops+1] = cost+p
                    heapq.heappush(visits,(cost+p,stops+1,d))
        out = min(costs[dst])
        return out if out < sys.maxsize else -1

    '''
    Use less memory than findCheapestPrice2 by using hash map instead of constant length list in costs.
    Complexity is the same as findCheapestPrice2, but it dynamically creates data for new stops when needed, which could save some storage in practice.
    Beat 99.8% runtime, 7% storage of all Leetcode submissions. It seems the saved storage is minor (7% vs 6%).
    '''
    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        h,visits,costs = defaultdict(list),[],[{} for i in range(n)]
        visits.append((0,-1,src))
        for s,d,p in flights:
            h[s].append([d,p])
        while visits:
            cost,stops,s = heapq.heappop(visits)
            if s == dst: return cost
            if stops+1 > K: continue
            for d,p in h[s]:
                new_stops = stops+1
                if new_stops not in costs[d]: costs[d][new_stops] = sys.maxsize
                if cost+p < costs[d][new_stops]:
                    costs[d][new_stops] = cost+p
                    heapq.heappush(visits,(cost+p,new_stops,d))
        out = min(costs[dst].values()) if len(costs[dst]) > 0 else sys.maxsize
        return out if out < sys.maxsize else -1

# Tests.
assert(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1) == 200)
assert(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0) == 500)
assert(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500],[1,0,300]], src = 0, dst = 2, K = 1) == 200)
assert(Solution().findCheapestPrice(10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7) == 14)
#assert(Solution().findCheapestPrice(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,13) == 47) # This one takes too long to run.
assert(Solution().findCheapestPrice2(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1) == 200)
assert(Solution().findCheapestPrice2(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0) == 500)
assert(Solution().findCheapestPrice2(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500],[1,0,300]], src = 0, dst = 2, K = 1) == 200)
assert(Solution().findCheapestPrice2(10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7) == 14)
assert(Solution().findCheapestPrice2(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,13) == 47)
assert(Solution().findCheapestPrice2(5,[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1) == -1)
assert(Solution().findCheapestPrice2(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1) == 6)
assert(Solution().findCheapestPrice2(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2) == 7)
assert(Solution().findCheapestPrice3(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1) == 200)
assert(Solution().findCheapestPrice3(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0) == 500)
assert(Solution().findCheapestPrice3(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500],[1,0,300]], src = 0, dst = 2, K = 1) == 200)
assert(Solution().findCheapestPrice3(10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7) == 14)
assert(Solution().findCheapestPrice3(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,13) == 47)
assert(Solution().findCheapestPrice3(5,[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1) == -1)
assert(Solution().findCheapestPrice3(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1) == 6)
assert(Solution().findCheapestPrice3(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2) == 7)
