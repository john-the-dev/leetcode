# 33. Search in Rotated Sorted Array
'''
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
'''
class Solution:
    '''
    A more complex binary search which is based on nums[b] and nums[k] in which b is the beginning element and k is the searched element.
    O(log(n)) runtime, O(1) storage.
    Beat 77% runtime, 38% storage of all Leetcode submissions.
    '''
    def search(self, nums, target):
        b,e = 0,len(nums)
        while b < e:
            k = (b+e)//2
            val = nums[k]
            if val == target: return k
            if val >= nums[b]:
                if val < target or nums[b] > target:
                    b = k+1
                else:
                    e = k
            else:
                if val > target or nums[b] <= target:
                    e = k
                else:
                    b = k+1
        return -1

assert(Solution().search([4,5,6,7,0,1,2], 0) == 4)
assert(Solution().search([4,5,6,7,0,1,2], 3) == -1)
assert(Solution().search([1], 0) == -1)
assert(Solution().search([4,5,6,7,0,1,2], 2) == 6)
assert(Solution().search([4,5,6,7,0,1,2], 3) == -1)
assert(Solution().search([3,1], 3) == 0)

