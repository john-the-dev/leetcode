# 46. Permutations
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    '''
    Recursion with a helper.
    O(n!) runtime, O(n!) storage.
    Beat 15% runtime, 97% storage of all Leetcode submissions.
    '''
    def permute(self, nums):
        def helper(arr):
            if len(arr) == 1: return [arr]
            out = []
            for i,num in enumerate(arr):
                remaining = arr[:i]
                remaining.extend(arr[i+1:])
                for row in helper(remaining):
                    out.append([num])
                    out[-1].extend(row)
            return out
        return helper(nums) if nums else []

# Tests.
assert(Solution().permute([1,2,3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert(Solution().permute([1]) == [[1]])
assert(Solution().permute([]) == [])
