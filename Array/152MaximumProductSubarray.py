# 152. Maximum Product Subarray
'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
from common import *
class Solution:
    '''
    Iterate and memorize two max products so far (1 for positive and 1 for negative).
    O(n) runtime, O(1) storage.
    Beat 31% runtime, 65% storage of all Leetcode submissions.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        out,curr = float('-inf'),[1,1]
        for i in range(len(nums)):
            if nums[i] == 0:
                out = max(out, nums[i])
                curr = [1,1]
            elif nums[i] > 0:
                curr[0],curr[1] = curr[0]*nums[i],curr[1]*nums[i]
                out = max(out, curr[0], curr[1])
            elif curr[1] > 0:
                curr[0],curr[1] = 1,curr[1]*nums[i]
                out = max(out, curr[1])
            else:
                curr[0],curr[1] = curr[1]*nums[i],curr[0]*nums[i]
                out = max(out, curr[0], curr[1])
        return out

# Tests.
assert(Solution().maxProduct([2,3,-2,4]) == 6)
assert(Solution().maxProduct([-2,0,-1]) == 0)
assert(Solution().maxProduct([2,3,-2,4,2]) == 8)
assert(Solution().maxProduct([2,-3,-2,4,2]) == 96)