# 74. Search a 2D Matrix
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
from common import *
class Solution:
    '''
    Translate row and column index from and to sorted array index.
    O(log(mn)) runtime, O(1) storage.
    Beat 96% runtime, 64% storage of all Leetcode submissions.
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        i,j = 0,m*n
        while i < j:
            k = (i+j) // 2
            k1,k2 = k // n,k % n
            if matrix[k1][k2] < target:
                i = k+1
            elif matrix[k1][k2] == target:
                return True
            else:
                j = k
        return False

# Tests.
assert(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3) == True)
assert(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13) == False)
