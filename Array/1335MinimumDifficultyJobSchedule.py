# 1335. Minimum Difficulty of a Job Schedule
'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 

Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843
 

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
'''
from common import *
class Solution:
    '''
    Dynamic programming, dp[i][j] in which i is # of days considered and j is the size of jobs considered so far.
    O(dn^2) runtime, O(nd) storage.
    Beat 62% runtime, 81% storage of all Leetcode submissions.
    '''
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [[-1 for j in range(n)] for i in range(d)]
        val,dp[0][0] = jobDifficulty[0],jobDifficulty[0]
        for j in range(1,n):
            val = max(jobDifficulty[j], val)
            dp[0][j] = val
        for i in range(1,d):
            for j in range(i,n):
                dp[i][j] = jobDifficulty[j]+dp[i-1][j-1]
                val = jobDifficulty[j]
                for k in range(j-1,i-1,-1):
                    val = max(val, jobDifficulty[k])
                    dp[i][j] = min(dp[i-1][k-1]+val,dp[i][j])
        return dp[d-1][n-1]

# Tests.
assert(Solution().minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2) == 7)
assert(Solution().minDifficulty(jobDifficulty = [9,9,9], d = 4) == -1)
assert(Solution().minDifficulty(jobDifficulty = [1,1,1], d = 3) == 3)
assert(Solution().minDifficulty(jobDifficulty = [7,1,7,1,7,1], d = 3) == 15)
assert(Solution().minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6) == 843)
        
