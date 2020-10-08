# 48. Rotate Image
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
 

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''
from common import *
class Solution:
    '''
    Rule matrix[i][j] -> matrix[j][n-i-1], dfs.
    O(n^2) runtime, O(1) storage.
    Beat 96% runtime, 13% storage of all Leetcode submissions.
    Note we need to define a bar and make sure the replaced values are not within the bar so that we can easily recognize them.
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0: return
        bar = max([max([abs(val) for val in row]) for row in matrix])  # All values are within [-bar,bar]
        addition = 2*bar+1  # Any modified value will be val+addition, so that the new values are within [bar+1,3*bar+1]
        def explore(i, j):
            i1,j1,val = j,n-i-1,matrix[i][j]
            while i1 != i or j1 != j:
                matrix[i1][j1],val = addition+val,matrix[i1][j1]
                i1,j1 = j1,n-i1-1
            matrix[i1][j1] = addition+val
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <= bar: explore(i, j)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j]-addition

# Tests.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
assert(matrix == [[7,4,1],[8,5,2],[9,6,3]])
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
assert(matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
matrix = [[1]]
Solution().rotate(matrix)
assert(matrix == [[1]])
matrix = [[43,39,3,33,37,20,14],[9,18,9,-1,40,22,38],[14,42,3,23,12,14,32],[18,31,45,11,8,-1,31],[28,44,14,23,40,24,13],[29,45,33,45,20,0,45],[12,23,35,32,22,39,8]]
Solution().rotate(matrix)
assert(matrix == [[12,29,28,18,14,9,43],[23,45,44,31,42,18,39],[35,33,14,45,3,9,3],[32,45,23,11,23,-1,33],[22,20,40,8,12,40,37],[39,0,24,-1,14,22,20],[8,45,13,31,32,38,14]])