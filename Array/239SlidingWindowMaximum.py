# 239. Sliding Window Maximum
'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
from common import *
class Solution:
    '''
    Left and right block by block then out[i-k+1] = max(left[i], right[i-k+1]
    O(n) runtime, O(n) storage.
    Beat 22% runtime, 83% storage of all Leetcode submissions.
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left,right,out,curr,count = [None]*n,[None]*n,[None]*(n-k+1),float('-inf'),0
        for i in range(n):
            curr = max(curr, nums[i])
            left[i] = curr
            count += 1
            if count == k: count,curr = 0,float('-inf')
        curr,begin = float('-inf'),count
        for i in range(begin):
            curr = max(curr, nums[n-i-1])
            right[n-i-1] = curr
        curr,count = float('-inf'),0
        for i in range(begin, n):
            curr = max(curr, nums[n-i-1])
            right[n-i-1] = curr
            count += 1
            if count == k: count,curr = 0,float('-inf')
        for i in range(k-1, n):
            out[i-k+1] = max(left[i], right[i-k+1])
        return out

# Tests.
assert(Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3) == [3,3,5,5,6,7])
assert(Solution().maxSlidingWindow(nums = [1], k = 1) == [1])
assert(Solution().maxSlidingWindow(nums = [1,-1], k = 1) == [1, -1])
assert(Solution().maxSlidingWindow(nums = [9,11], k = 2) == [11])
assert(Solution().maxSlidingWindow(nums = [4,-2], k = 2) == [4])
assert(Solution().maxSlidingWindow(nums = [7,2,4], k = 2) == [7,4])
