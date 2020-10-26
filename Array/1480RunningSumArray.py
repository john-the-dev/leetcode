# 1480. Running Sum of 1d Array
'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''
from common import *
class Solution:
    '''
    Use previous sum to calculate current sum.
    O(n) runtime, O(1) storage.
    Beat 64% runtime, 99.9% storage of all Leetcode submissions.
    '''
    def runningSum(self, nums: List[int]) -> List[int]:
        out,n = [],len(nums)
        if n == 0: return out
        out.append(nums[0])
        for i in range(1,n):
            out.append(out[i-1]+nums[i])
        return out

# Tests.
assert(Solution().runningSum([1,2,3,4]) == [1,3,6,10])
assert(Solution().runningSum([1,1,1,1,1]) == [1,2,3,4,5])
assert(Solution().runningSum([3,1,2,10,1]) == [3,4,6,16,17])