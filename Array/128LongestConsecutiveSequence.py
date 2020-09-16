# 128. Longest Consecutive Sequence
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class Solution:
    '''
    Set with removals.
    O(n) runtime, O(n) storage.
    Beat 79% runtime, 58% storage of all Leetcode submissions.
    '''
    def longestConsecutive(self, nums):
        s,out = set(nums),0
        while s:
            num = None
            for val in s:
                num = val
                break
            s.remove(num)
            l,num1,num2 = 1,num+1,num-1
            while s and num1 in s:
                s.remove(num1)
                l += 1
                num1 += 1
            while s and num2 in s:
                s.remove(num2)
                l += 1
                num2 -= 1
            out = max(out, l)
        return out

assert(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
assert(Solution().longestConsecutive([]) == 0)
assert(Solution().longestConsecutive([100, 4, 6, 1, 3, 2]) == 4)
assert(Solution().longestConsecutive([100, 4, 200, -1, 0, 3, 1]) == 3)