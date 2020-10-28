# 540. Single Element in a Sorted Array
'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
'''
from common import *
class Solution:
    '''
    Binary search. The search direction is based on whether the index is odd or even.
    O(log(n)) runtime, O(1) storage.
    Beat 99% runtime, 100% storage of all Leetcode submissions.
    Note we need to find the span (same two numbers) instead of 1 index for each iteration.
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i,j = 0,len(nums)
        while i < j:
            k = (i+j) // 2
            if k > 0 and nums[k-1] == nums[k]: k -= 1
            if (k < j-1 and nums[k] != nums[k+1]) or k == j-1: return nums[k]
            if k % 2 == 0:
                i = k+2
            else:
                j = k
        
# Tests.
assert(Solution().singleNonDuplicate([1]) == 1)
assert(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2)
assert(Solution().singleNonDuplicate([3,3,7,7,10,11,11]) == 10)
