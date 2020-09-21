# 240. Search a 2D Matrix II
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution:
    '''
    Binary search on matrix. Every time a block is excluded.
    O(nlog(n)) runtime, O(log(n)) storage, assuming m ~= n.
    Beat 81% runtime, 29% storage of all Leetcode submissions.
    '''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        def search(i1,j1,i2,j2):
            if i1 == i2 or j1 == j2: return False
            i3,j3 = (i1+i2) // 2,(j1+j2) // 2
            v = matrix[i3][j3]
            if v == target: 
                return True
            elif v < target:
                if search(i1,j3+1,i2,j2): return True
                if search(i3+1,j1,i2,j3+1): return True
            else:
                if search(i1,j1,i2,j3): return True
                if search(i1,j3,i3,j2): return True
            return False
        return search(0,0,m,n)

# Tests.
assert(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5) == True)
assert(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20) == False)
assert(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],1) == True)
assert(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],30) == True)
assert(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],31) == False)
assert(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],0) == False)
            