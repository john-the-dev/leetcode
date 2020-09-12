# 54. Spiral Matrix
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Accepted
397,220
Submissions
1,156,789
'''
class Solution:
    '''
    Simulate spiral order: starting direction is right, keep going until reaching deadend and then turning right (down). Repeat this rule until all items are explored.
    Replace explored item with None and use it for deadend check.
    O(mn) runtime, O(1) storage.
    Beat 59% runtime, 50% storage of all Leetcode submissions.
    '''
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0: return []
        i,j,n,out = 0,0,len(matrix[0]),[]
        d = 0 # 0 is right, 1 is down, 2 is left, 3 is up
        while i >= 0 and j >= 0 and i < m and j < n and matrix[i][j] != None:
            out.append(matrix[i][j])
            matrix[i][j] = None
            if d == 0:
                if j < n-1 and matrix[i][j+1] != None: # Deadend is not hit yet.
                    j += 1
                else: # Deadend is hit.
                    d += 1
                    i += 1
            elif d == 1:
                if i < m-1 and matrix[i+1][j] != None:
                    i += 1
                else:
                    d += 1
                    j -= 1
            elif d == 2:
                if j > 0 and matrix[i][j-1] != None:
                    j -= 1
                else:
                    d += 1
                    i -= 1
            elif d == 3:
                if i > 0 and matrix[i-1][j] != None:
                    i -= 1
                else:
                    d = 0
                    j += 1
        return out

assert(Solution().spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]) == [1,2,3,6,9,8,7,4,5])
assert(Solution().spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7])
assert(Solution().spiralOrder([[ 1, 2, 3 ]]) == [1,2,3])
assert(Solution().spiralOrder([[1],[2],[3]]) == [1,2,3])
assert(Solution().spiralOrder([]) == [])

