# 11. Container With Most Water
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
from common import *
class Solution:
    '''
    Sliding window from left and right side, move lower side as all higher side has been exlcuded.
    O(n) runtime, O(1) storage.
    Beat 16% runtime, 29% storage of all Leetcode submissions.
    '''
    def maxArea(self, height: List[int]) -> int:
        i,j,out = 0,len(height)-1,0
        while i < j:
            out = max(out, min(height[i], height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return out

# Tests.
assert(Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49)   
assert(Solution().maxArea([1,1]) == 1)
assert(Solution().maxArea([4,3,2,1,4]) == 16)
assert(Solution().maxArea([1,2,1]) == 2)