# 53. Maximum Subarray
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
'''
import sys
class Solution:
    '''
    Memorization of smallest number so far and then find biggest gap in between.
    O(n) runtime, O(1) storage.
    Beat 66% runtime, 6% storage of all Leetcode submissions.
    '''
    def maxSubArray(self, nums):
        out,smallest,val = -sys.maxsize-1,0,0
        for i in range(len(nums)):
            val += nums[i]
            out = max(out,val-smallest)
            smallest = min(val, smallest)
        return out

# Tests.
assert(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
assert(Solution().maxSubArray([1]) == 1)
assert(Solution().maxSubArray([0]) == 0)
assert(Solution().maxSubArray([-2147483647]) == -2147483647)
assert(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-20,25]) == 25)
assert(Solution().maxSubArray([-2,-1]) == -1)
assert(Solution().maxSubArray([1,2]) == 3)
