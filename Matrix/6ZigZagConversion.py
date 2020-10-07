# 6. ZigZag Conversion
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
from common import *
class Solution:
    '''
    Rule: direction (default down) and update based on condition.
    O(N) runtime, O(N+m) storage in which N is the size of s and m is number of rows.
    Beat 82% runtime, 14% storage of all Leetcode submisions.
    '''
    def convert(self, s: str, numRows: int) -> str:
        down,out,n,r = True,[[] for i in range(numRows)],len(s),0
        for c in s:
            out[r].append(c)
            if down:
                if r < numRows-1:
                    r += 1
                else:
                    r -= 1
                    down = not down
            else:
                if r > 0:
                    r -= 1
                else:
                    r += 1
                    down = not down
        return ''.join([''.join(row) for row in out])

assert(Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
assert(Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
assert(Solution().convert("A", 1) == "A")