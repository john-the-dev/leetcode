# 209. Minimum Size Subarray Sum
'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''
from common import *
import sys
class Solution:
    '''
    Sliding window from left, slide j to reach target, slide i to shrink.
    O(n) runtime, O(1) storage.
    Beat 54% runtime, 79% storage of all Leetcode submissions.
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i,j,n,out = 0,0,len(nums),[sys.maxsize, 0]
        while i < n:
            while j < n and out[1] < s:
                out[1] += nums[j]
                j += 1
            if out[1] >= s: out[0] = min(out[0], j-i)
            out[1] -= nums[i]
            i += 1
        return out[0] if out[0] != sys.maxsize else 0

# Tests.
assert(Solution().minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]) == 2)
assert(Solution().minSubArrayLen(s = 4, nums = [1,4,4]) == 1)
assert(Solution().minSubArrayLen(s = 11, nums = [1,1,1,1,1,1,1,1]) == 0)
        