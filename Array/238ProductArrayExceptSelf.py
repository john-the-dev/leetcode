# 238. Product of Array Except Self
'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
from common import *
class Solution:
    '''
    Use left and right array. left[i] = product of nums[:i], right[i] = product of nums[-(i+1):] then out[i] = left[i-1]*right[n-i-2]
    O(n) runtime, O(n) storage.
    Beat 26% runtime, 9% storage of all Leetcode submissions.
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right,n = [nums[0]],[nums[-1]],len(nums)
        for i in range(1,n):
            left.append(nums[i]*left[-1])
        for i in range(n-2,-1,-1):
            right.append(nums[i]*right[-1])
        out = []
        for i in range(n):
            left_val = 1 if i == 0 else left[i-1]
            right_val = 1 if i == n-1 else right[n-i-2]
            out.append(left_val*right_val)
        return out

    '''
    Use constant space by reusing input and output.
    O(n) runtime, O(1) storage.
    Beat 26% runtime, 13% storage of all Leetcode submissions.
    '''
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0]*n
        out[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            out[i] = nums[i]*out[i+1]
        for i in range(1,n):
            nums[i] = nums[i-1]*nums[i]
        for i in range(n):
            left_val = 1 if i == 0 else nums[i-1]
            right_val = 1 if i == n-1 else out[i+1]
            out[i] = left_val*right_val
        return out

# Tests.
assert(Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6])
assert(Solution().productExceptSelf2([1,2,3,4]) == [24,12,8,6])

        