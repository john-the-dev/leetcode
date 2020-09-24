# 31. Next Permutation
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution:
    '''
    Rule: 1) Find from right side nums[i-1] < nums[i]; 2) Find from right side the first nums[j] > nums[i-1], swap nums[i-1] and nums[j]; 3) Reverse nums[i:].
    O(n) runtime, O(1) storage.
    Beat 10% runtime and 56% storage of all Leetcode submissions.
    '''
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        found,n = False,len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                found = True
                break
        if found:
            for j in range(n-1,i-1,-1):
                if nums[j] > nums[i-1]:
                    nums[i-1],nums[j] = nums[j],nums[i-1]
                    break
        else:
            i = 0
        j = n-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1

# Tests.
nums = [1,2,3]
Solution().nextPermutation(nums)
assert(nums == [1,3,2])
nums = [3,2,1]
Solution().nextPermutation(nums)
assert(nums == [1,2,3])
nums = [1,1,5]
Solution().nextPermutation(nums)
assert(nums == [1,5,1])
nums = [1,2,3,2,1]
Solution().nextPermutation(nums)
assert(nums == [1,3,1,2,2])
nums = [1,3,2]
Solution().nextPermutation(nums)
assert(nums == [2,1,3])