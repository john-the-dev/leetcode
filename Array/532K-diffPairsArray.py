# 532. K-diff Pairs in an Array
'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Example 4:

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2
Example 5:

Input: nums = [-1,-2,-3], k = 1
Output: 2
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
'''
from common import *
from collections import defaultdict
class Solution:
    '''
    Memorization with set to remember what we have seen so search can be O(1).
    O(n) runtime, O(n) storage.
    Beat 18% runtime, 20% storage of all Leetcode submissions.
    '''
    def findPairs(self, nums: List[int], k: int) -> int:
        out = 0
        if k == 0:
            h = defaultdict(int)
            for num in nums:
                h[num] += 1
            for num in h:
                if h[num] > 1: out += 1
        else:
            s = set(nums)
            seen = set()
            for num in s:
                if num+k in seen: out += 1
                if num-k in seen: out += 1
                seen.add(num)
        return out

# Tests.
assert(Solution().findPairs([3,1,4,1,5], 2) == 2)
assert(Solution().findPairs([1,2,3,4,5], 1) == 4)
assert(Solution().findPairs([1,3,1,5,4], 0) == 1)
assert(Solution().findPairs([1,2,4,4,3,3,0,9,2,3], 3) == 2)
assert(Solution().findPairs([-1,-2,-3], 1) == 2)
assert(Solution().findPairs([1,1,1,1,1], 0) == 1)