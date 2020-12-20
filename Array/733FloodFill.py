# 733. Flood Fill
'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''
from common import *
class Solution:
    '''
    Breath first search to replace the locations with the new color.
    O(mn) runtime, O(m+n) storage as worst case there needs 2m+2n items in layer.
    Beat 5% runtime, 52% storage of all Leetcode submissions.
    Note Depth first search will need O(mn) storage for the call stack. So it is worse than BFS.
    '''
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        layer,oldColor,image[sr][sc],m,n = set([(sr,sc)]),image[sr][sc],newColor,len(image),len(image[0])
        if oldColor == newColor: return image
        while layer:
            new_layer = set()
            for r,c in layer:
                if r > 0 and image[r-1][c] == oldColor: 
                    new_layer.add((r-1,c))
                    image[r-1][c] = newColor
                if r < m-1 and image[r+1][c] == oldColor: 
                    new_layer.add((r+1,c))
                    image[r+1][c] = newColor
                if c > 0 and image[r][c-1] == oldColor: 
                    new_layer.add((r,c-1))
                    image[r][c-1] = newColor
                if c < n-1 and image[r][c+1] == oldColor: 
                    new_layer.add((r,c+1))
                    image[r][c+1] = newColor
            layer = new_layer
        return image

# Tests.
assert(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2) == [[2,2,2],[2,2,0],[2,0,1]])
            


