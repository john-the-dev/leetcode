# 523. Continuous Subarray Sum
'''
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''
class Solution:
    '''
    Hash map to memorize sum[:i] % k so that when see it again at j we know there is a subarray [i+1:j+1] whose sum is multiples of k.
    O(n) runtime, O(min(k,n)) storage.
    Beat 99.7% runtime, 6.7% storage of all Leetcode submissions. The reason for bad storage is that brute forcing has O(1).
    '''
    def checkSubarraySum(self, nums, k):
        h,n,v = {0:-1},len(nums),0
        if k == 0:
            for i in range(n-1):
                if nums[i] == 0 and nums[i+1] == 0: return True
        else:
            for i in range(n):
                v += nums[i]
                m = v % k
                if m in h:
                    if i-h[m] >= 2: return True
                else:
                    h[m] = i
        return False

# Tests.
assert(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6) == True)
assert(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6) == True)
assert(Solution().checkSubarraySum([23, 2, 7], 6) == False)
assert(Solution().checkSubarraySum([], 6) == False)
assert(Solution().checkSubarraySum([23,2,6,4,7], 0) == False)
assert(Solution().checkSubarraySum([6,4,7], 6) == False)