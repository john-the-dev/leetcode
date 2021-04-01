# 759. Employee Free Time
'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
'''

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

from common import *
import sys
import heapq
class Solution:
    '''
    Calculate free time for each employee, then merge the free time.
    O(N^2) runtime, O(N) storage, in which N is # of Intervals.
    Beat 5% runtime, 86% storage of all Leetcode submissions.
    '''
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        freetime,low,high = [],sys.maxsize,-sys.maxsize-1
        for employee in schedule:
            for worktime in employee:
                low = min(low, worktime.start)
                high = max(high, worktime.end)
        for employee in schedule:
            freetime.append([])
            if employee[0].start > low: freetime[-1].append(Interval(low,employee[0].start))
            for i in range(1,len(employee)):
                if employee[i].start > employee[i-1].end: freetime[-1].append(Interval(employee[i-1].end,employee[i].start))
            if employee[-1].end < high: freetime[-1].append(Interval(employee[-1].end,high)) 
        def merge(free1, free2):
            free,i1,i2,n1,n2 = [],0,0,len(free1),len(free2)
            while i1 < n1 and i2 < n2:
                if free1[i1].start > free2[i2].start: free1,free2,i1,i2,n1,n2 = free2,free1,i2,i1,n2,n1
                if free1[i1].end > free2[i2].start:
                    if free1[i1].end > free2[i2].end:
                        free.append(Interval(free2[i2].start,free2[i2].end))
                        i2 += 1
                    else:
                        free.append(Interval(free2[i2].start,free1[i1].end))
                        i1 += 1
                else:
                    i1 += 1
            return free
        out = freetime[0]
        for i in range(1,len(freetime)):
            out = merge(out,freetime[i])
        return out

    '''
    Priority queue to find all busy intervals first, then compute free time.
    O(Nlog(k)) runtime, O(k) storage, in which N is # of intervals, k is # of employees.
    Beat 25% runtime, 76% storage of all Leetcode submissions.
    '''
    def employeeFreeTime2(self, schedule: '[[Interval]]') -> '[Interval]':
        k = len(schedule)
        q,out = [],[]
        for i in range(k):
            if len(schedule[i]) > 0: q.append([schedule[i][0].start,schedule[i][0].end,i,0])
        heapq.heapify(q)
        while q:
            start,end,i,j = heapq.heappop(q)
            if not out or out[-1][1] < start:
                out.append([start,end])
            else:
                out[-1][1] = max(out[-1][1],end)
            if j < len(schedule[i])-1: heapq.heappush(q,[schedule[i][j+1].start,schedule[i][j+1].end,i,j+1])
        for i in range(1,len(out)):
            out[i-1] = Interval(out[i-1][1],out[i][0])
        if out: out.pop()
        return out

# Tests.
def assert_out(expected_out, actual_out):
    assert(len(expected_out) == len(actual_out))
    for i in range(len(expected_out)):
        assert(expected_out[i].start == actual_out[i].start)
        assert(expected_out[i].end == actual_out[i].end)    
expected_out = [Interval(3,4)]
actual_out = Solution().employeeFreeTime([[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]])
assert_out(expected_out, actual_out)
expected_out = [Interval(5,6),Interval(7,9)]
actual_out = Solution().employeeFreeTime([[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]])
assert_out(expected_out, actual_out)
expected_out = [Interval(3,4)]
actual_out = Solution().employeeFreeTime2([[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]])
assert_out(expected_out, actual_out)
expected_out = [Interval(5,6),Interval(7,9)]
actual_out = Solution().employeeFreeTime2([[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]])
assert_out(expected_out, actual_out)

                