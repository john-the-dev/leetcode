# 1. Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
from common import *
class Solution:
    '''
    Hash map to momorize what have been seen and its index.
    O(n) runtime, O(n) storage.
    Beat 66% runtime, 22% storage of all Leetcode submissions.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,num in enumerate(nums):
            if num in h: return [h[num],i]
            h[target-num] = i
        
# Tests.
assert(Solution().twoSum([2,7,11,15],9) == [0,1])
assert(Solution().twoSum([3,2,4],6) == [1,2])
assert(Solution().twoSum([3,3],6) == [0,1])
assert(Solution().twoSum([2,7,11,15,6],22) == [1,3])
        