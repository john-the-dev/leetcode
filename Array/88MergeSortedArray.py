# 88. Merge Sorted Array
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''
from common import *
class Solution:
    '''
    Move nums1 to right side, then merge nums1 and nums2 with two pointers.
    O(2m+n) runtime, O(1) storage.
    Beat 64% runtime, 45% storage of all Leetcode submissions.
    Note that when moving the items in nums1 to right side, move from m-1 towards 0, because from 0 towards m-1 may result in unrecovarable items.
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1,-1,-1):
            nums1[i],nums1[i+n] = nums1[i+n],nums1[i]
        i,j,k = 0,0,0
        while k < m+n:
            if i == m:
                nums1[k] = nums2[j]
                j += 1
            elif j == n:
                nums1[k] = nums1[i+n]
                i += 1
            elif nums1[i+n] < nums2[j]:
                nums1[k] = nums1[i+n]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
# Tests.
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
Solution().merge(nums1,3,nums2,3)
assert(nums1 == [1,2,2,3,5,6])
nums1 = [5,6,7,0,0,0]
nums2 = [1,2,3]
Solution().merge(nums1,3,nums2,3)
assert(nums1 == [1,2,3,5,6,7])
nums1 = [7,7,0,0,0]
nums2 = [7,7,7]
Solution().merge(nums1,2,nums2,3)
assert(nums1 == [7,7,7,7,7])
nums1 = [1,2,4,5,6,0]
nums2 = [3]
Solution().merge(nums1,5,nums2,1)
assert(nums1 == [1,2,3,4,5,6])