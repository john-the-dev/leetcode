# 42. Trapping Rain Water
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    '''
    Special sliding window approach which slides from very left and right side. For each iteration, slide the side with shorter wall.
    O(n) runtime, O(1) storage.
    Beat 89% runtime, 21% storage of all Leetcode submissions.
    Note typically sliding window goes from 1 side. This is a special case that there is tricky relationship between left and right side (i.e., they together form walls and shorter wall height determines the water volume).
    '''
    def trap(self, height):
        i,j,out = 0,len(height)-1,0
        while i < j:
            if height[i] < height[j]:
                k = i+1
                while k < j and height[k] <= height[i]:
                    out += height[i]-height[k]
                    k += 1
                i = k
            else:
                k = j-1
                while k > i and height[k] <= height[j]:
                    out += height[j]-height[k]
                    k -= 1
                j = k
        return out

assert(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)