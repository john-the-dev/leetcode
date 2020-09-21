# 453. Minimum Moves to Equal Array Elements
'''
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
[1,2,3]  =>  [1,2,2]  =>  [1,2,1]  =>  [1,1,1]
'''
class Solution:
    '''
    Transform the problem to minimum diff: instead of increase n-1 elements, it is equivalent to decrease the max element each time; total steps is the sum of the diff between every element and minimum element.
    O(n) runtime, O(1) storage.
    Beat 73% runtime, 64% storage of all Leetcode submissions.
    '''
    def minMoves(self, nums):
        v,out = min(nums),0
        for num in nums:
            out += num-v
        return out

assert(Solution().minMoves([1,2,3]) == 3)
assert(Solution().minMoves([1]) == 0)
assert(Solution().minMoves([1,2,3,5]) == 7)