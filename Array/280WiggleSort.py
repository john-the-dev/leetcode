# 280. Wiggle Sort
'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''
from common import *
class Solution:
    '''
    Loop through and exchange if nums[i] and nums[i+1] not satisfy rule.
    O(n) runtime, O(1) storage.
    Beat 84% runtime, 99% storage of all Leetcode submissions.
    '''
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]: nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
                if nums[i] < nums[i+1]: nums[i],nums[i+1] = nums[i+1],nums[i]
        
# Tests.
nums = [3,5,2,1,6,4]
Solution().wiggleSort(nums)
assert(nums == [3,5,1,6,2,4])
nums = [1,2,3]
Solution().wiggleSort(nums)
assert(nums == [1,3,2])
nums = [2,1]
Solution().wiggleSort(nums)
assert(nums == [1,2])
