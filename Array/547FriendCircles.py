# 547. Friend Circles
'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

 

Constraints:

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
'''
from common import *
class Solution:
    '''
    Union find with disjoint set union.
    O(N^2log(N)) runtime, O(N) storage.
    Beat 79% runtime, 6% storage of all Leetcode submissions.
    '''
    def findCircleNum(self, M: List[List[int]]) -> int:
        N,groups = len(M),DSU()
        for i in range(N):
            for j in range(i+1,N):
                if M[i][j] == 1:
                    groups.union(i,j)
        out = set()
        for k in range(N):
            out.add(groups.find(k))
        return len(out)

# Tests.
assert(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2)
assert(Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]]) == 1)
