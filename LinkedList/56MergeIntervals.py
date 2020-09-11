# 56. Merge Intervals
'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

intervals[i][0] <= intervals[i][1]
'''
class Solution:
    '''
    sort, merge based on rule.
    O(nlog(n)) runtime, O(1) storage.
    Beat 94% runtime, 61% storage among all Leetcode submissions.
    '''
    def merge(self, intervals):
        intervals.sort()
        n = len(intervals)
        if n == 0: return intervals
        curr,out = intervals[0],[]
        for i in range(1,n):
            interval = intervals[i]
            if curr[1] < interval[0]:
                out.append(curr)
                curr = interval
            else:
                curr[1] = max(interval[1],curr[1])
        out.append(curr)
        return out

# Tests.
assert(Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])
assert(Solution().merge([[1,4],[4,5]]) == [[1,5]])
assert(Solution().merge([[1,3],[2,6],[3,10],[15,18]]) == [[1,10],[15,18]])
assert(Solution().merge([]) == [])
assert(Solution().merge([[1,3]]) == [[1,3]])
assert(Solution().merge([[1,4],[2,3]]) == [[1,4]])

