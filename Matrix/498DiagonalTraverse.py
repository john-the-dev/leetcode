# 498. Diagonal Traverse
'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
'''
from common import *
class Solution:
    '''
    Rule: define a direction (up or down) and update it accordingly based on the current location.
    O(mn) runtime, O(1) storage.
    Beat 99% runtime, 70% storage of all Leetcode submissions.
    '''
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        i,j,up,out = 0,0,True,[]
        while i < m and j < n:
            out.append(matrix[i][j])
            if up:
                if i == 0:
                    if j < n-1:
                        j += 1
                    else:
                        i += 1
                    up = not up
                elif j == n-1:
                    i += 1
                    up = not up
                else:
                    j += 1
                    i -= 1
            else:
                if j == 0:
                    if i < m-1:
                        i += 1
                    else:
                        j += 1
                    up = not up
                elif i == m-1:
                    j += 1
                    up = not up
                else:
                    i += 1
                    j -= 1
        return out
        
# Tests.
assert(Solution().findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]) == [1,2,4,7,5,3,6,8,9])
assert(Solution().findDiagonalOrder([[1]]) == [1])
assert(Solution().findDiagonalOrder([[1,2]]) == [1,2])
assert(Solution().findDiagonalOrder([[1],[2]]) == [1,2])
assert(Solution().findDiagonalOrder([]) == [])
            
