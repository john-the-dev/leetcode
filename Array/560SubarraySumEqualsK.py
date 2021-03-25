# 560. Subarray Sum Equals K
'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    Cumulative sum (diff will be the consecutive sum) + hashmap (check for previously seen sum.).
    O(n) runtime, O(n) storage.
    Beat 24% runtime, 19% storage of all Leetcode submissions.
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        seen,out = defaultdict(int),0
        seen[0] = 1
        for i,num in enumerate(nums):
            v = num-k
            out += seen[v]
            seen[num] += 1
        return out

# Tests.
assert(Solution().subarraySum([1,1,1], 2) == 2)
assert(Solution().subarraySum([1,2,3], 3) == 2)
