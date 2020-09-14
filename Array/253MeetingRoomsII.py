# 253. Meeting Rooms II
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
import heapq
class Solution:
    '''
    Sorting + priority queue.
    O(nlog(n)) runtime, O(m) storage, in which n is length of intervals and m is minimum # of rooms.
    Beat 27% runtime, 62% storage of all Leetcode submissions.
    '''
    def minMeetingRooms(self, intervals):
        q = []
        intervals.sort()
        for interval in intervals:
            if q and q[0] <= interval[0]: heapq.heappop(q) # We can reuse a room.
            heapq.heappush(q, interval[1])
        return len(q)

# Tests.
assert(Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]) == 2)
assert(Solution().minMeetingRooms([[7,10],[2,4]]) == 1)
assert(Solution().minMeetingRooms([[5, 10],[15, 20],[0, 30]]) == 2)
assert(Solution().minMeetingRooms([]) == 0)
assert(Solution().minMeetingRooms([[5, 10]]) == 1)
            