# 324. Wiggle Sort II
'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
Note requirement for O(1) cannot be satisified.
'''
from common import *
import heapq
class Solution:
    '''
    Find median, then median,up,median,up,low,up,low,up,....
    O(nlog(n)) runtime, O(n) storage.
    Beat 41% runtime, 6% storage.
    '''
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        half = n // 2
        def getMedian(nums):
            q,out = nums.copy(),None
            heapq.heapify(q)
            while len(q) > half:
                out = heapq.heappop(q)
            if n % 2 == 0: out = (heapq.heappop(q)+out) // 2
            return out
        median,copy = getMedian(nums),nums.copy()
        ups,lows,m = [],[],0
        for i,num in enumerate(nums):
            if num > median: 
                ups.append(i)
            elif num < median:
                lows.append(i)
            else:
                m += 1
        j = half-len(lows)
        if n % 2 == 1: j += 1
        for i in range(n):
            if i % 2 == 0:
                if j > 0:
                    nums[i] = median
                    j -= 1
                else:
                    nums[i] = copy[lows.pop()]
            else:
                if len(ups) > 0:
                    nums[i] = copy[ups.pop()]
                else:
                    nums[i] = median    

# Tests.
nums = [1, 5, 1, 1, 6, 4]
Solution().wiggleSort(nums)
assert(nums == [1, 4, 1, 6, 1, 5])
nums = [1, 3, 2, 2, 3, 1]
Solution().wiggleSort(nums)
assert(nums == [2, 3, 1, 3, 1, 2])
nums = [1, 3, 2, 2, 3]
Solution().wiggleSort(nums)
assert(nums == [2, 3, 2, 3, 1])
nums = [1]
Solution().wiggleSort(nums)
assert(nums == [1])
nums = [2,1]
Solution().wiggleSort(nums)
assert(nums == [1,2])
nums = [4,5,5,6]
Solution().wiggleSort(nums)
assert(nums == [5,6,4,5])
        
        
        
