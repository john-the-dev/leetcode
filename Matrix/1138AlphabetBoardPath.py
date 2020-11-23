# 1138. Alphabet Board Path
'''
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

 

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"
 

Constraints:

1 <= target.length <= 100
target consists only of English lowercase letters.
'''
class Solution:
    '''
    Rule: from current position to next position is simply moving with minimum steps. Only exception is how to handle 'z'.
    O(n) runtime, O(1) storage, in which n is the size of target.
    Beat 95% runtime, 10% storage of all Leetcode submissions.
    '''
    def alphabetBoardPath(self, target: str) -> str:
        board,num = {},ord('a')
        for i in range(5):
            for j in range(5):
                board[chr(num)] = (i,j)
                num += 1
        board[chr(num)] = (5,0)
        i1,j1,out = 0,0,[]
        for c in target:
            i2,j2 = board[c]
            if c != 'z':
                if i2 > i1:
                    out.extend(['D']*(i2-i1))
                else:
                    out.extend(['U']*(i1-i2))
                if j2 > j1:
                    out.extend(['R']*(j2-j1))
                else:
                    out.extend(['L']*(j1-j2))
            else:
                if j2 > j1:
                    out.extend(['R']*(j2-j1))
                else:
                    out.extend(['L']*(j1-j2))
                if i2 > i1:
                    out.extend(['D']*(i2-i1))
                else:
                    out.extend(['U']*(i1-i2))
            out.append('!')
            i1,j1 = i2,j2
        return ''.join(out)

# Tests.
assert(Solution().alphabetBoardPath("leet") == "DDR!UURRR!!DDD!")
assert(Solution().alphabetBoardPath("code") == "RR!DDRR!UUL!R!")
assert(Solution().alphabetBoardPath("ze") == "DDDDD!UUUUURRRR!")
assert(Solution().alphabetBoardPath("zdz") == "DDDDD!UUUUURRR!LLLDDDDD!")