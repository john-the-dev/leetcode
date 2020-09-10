# 15. 3Sum
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
from common import *
class Solution:
    '''
    Use 1 loop to convert the problem to 2Sum problem. Then we can solve 2Sum problem with O(n). So total would be O(n^2) runtime. Storage complexity is O(n) because we use set to memorize seen data.
    This code will get Time Limit Exceeded error when submitting to leetcode.com.
    '''
    def threeSum(self, nums):
        n,out = len(nums),set()
        for i in range(n):
            target,seen = 0-nums[i],{}
            for j in range(n):
                if j == i: continue
                num = nums[j]
                if num in seen:
                    item = [nums[i],num,seen[num]]
                    item.sort()
                    out.add(tuple(item))
                else:
                    seen[target-num] = num
        return [list(item) for item in out]

    '''
    Performance improved version with: 1) sorting; 2) sliding window in sorted array. We can use sort and not increase complexity because sorting is O(nlog(n)) and we will have O(n^2) anyway for the total solution. Also note that we avoided using set to check duplicate output.
    This version beats 77% of leetcode submissions on runtime and 44% on storage.
    '''
    def threeSum2(self, nums):
        nums.sort()
        i,n,out = 0,len(nums),[]
        while i < n:
            j,k = i+1,n-1
            while j < k:
                val = nums[i]+nums[j]+nums[k]
                if val < 0:
                    j += 1
                elif val > 0:
                    k -= 1
                else:
                    out.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
                    while k >= 0 and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
        return out

# Tests.
assert_list_noorder(Solution().threeSum([-1,0,1,2,-1,-4]),[[-1,-1,2],[-1,0,1]])
assert_list_noorder(Solution().threeSum([]),[])
assert_list_noorder(Solution().threeSum([0]),[])
assert_list_noorder(Solution().threeSum2([-1,0,1,2,-1,-4]),[[-1,-1,2],[-1,0,1]])
assert_list_noorder(Solution().threeSum2([]),[])
assert_list_noorder(Solution().threeSum2([0]),[])
