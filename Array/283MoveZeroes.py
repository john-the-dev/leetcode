# 283. Move Zeroes
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''
from common import *
class Solution:
    '''
    Two pointers, 1 points to beginning of processing item, 1 points to beginning of moving position.
    O(n) runtime, O(1) storage.
    Beat 77% runtime, 20% storage of all Leetcode submissions.
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,n = 0,0,len(nums)
        while j < n:
            while j < n and nums[j] == 0:
                j += 1
            if j < n:
                if i != j: nums[i] = nums[j]
                j += 1
                i += 1
        while i < n:
            nums[i] = 0
            i += 1
        
# Tests.
nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
assert(nums == [1,3,12,0,0])
nums = [0]
Solution().moveZeroes(nums)
assert(nums == [0])