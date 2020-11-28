# 1209. Remove All Adjacent Duplicates in String II
'''
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
'''
from common import *
class Solution:
    '''
    Counter and continous update.
    O(nd) runtime, O(n) storage, in which n is length of the string and d is the # of iterations on k duplicate removal on the string.
    Beat 51% runtime, 24% storage of all Leetcode submissions.
    Note that we need to merge two items if the item in the middle needs to be remove and the two items are the same character.
    '''
    def removeDuplicates(self, s: str, k: int) -> str:
        out,n = [],len(s)
        if n == 0: return ''
        out.append([s[0],1])
        for i in range(1,n):
            if out[-1][0] == s[i]:
                out[-1][1] += 1
            else:
                out.append([s[i],1])
        done = False
        while not done:
            out2,i,n,done = [],0,len(out),True
            while i < n:
                if out[i][1] < k:
                    out2.append(out[i])
                elif out[i][1] > k and out[i][1] % k > 0:
                    out[i][1] = out[i][1] % k
                    out2.append(out[i])
                    done = False
                else:
                    if out2 and i < n-1 and out2[-1][0] == out[i+1][0]:
                        out2[-1][1] += out[i+1][1]
                        i += 1
                    done = False
                i += 1
            out = out2
        for i in range(len(out)):
            out[i] = out[i][0]*out[i][1]
        return ''.join(out)

    '''
    Stack based, with counter.
    O(n) runtime, O(n) storage.
    Beat 60% runtime, 16% storage of all Leetcode submissions.
    Note that we can finish all removals with 1 iteration because there is 1 trigger character for each removal.
    '''
    def removeDuplicates2(self, s: str, k: int) -> str:
        out,n = [],len(s)
        if n == 0: return ''
        out.append([s[0],1])
        for i in range(1,n):
            if out[-1][0] == s[i]:
                out[-1][1] += 1
            else:
                out.append([s[i],1])
        stack = []
        for i in range(len(out)):
            if not stack or stack[-1][0] != out[i][0]:
                stack.append(out[i])
            else:
                stack[-1][1] += out[i][1]
            stack[-1][1] = stack[-1][1] % k
            if stack[-1][1] == 0: stack.pop()
        for i in range(len(stack)):
            stack[i] = stack[i][0]*stack[i][1]
        return ''.join(stack)

# Tests.
assert(Solution().removeDuplicates("abcd", 2) == "abcd")
assert(Solution().removeDuplicates("deeedbbcccbdaa", 3) == "aa")
assert(Solution().removeDuplicates("pbbcggttciiippooaais", 2) == "ps")
assert(Solution().removeDuplicates2("abcd", 2) == "abcd")
assert(Solution().removeDuplicates2("deeedbbcccbdaa", 3) == "aa")
assert(Solution().removeDuplicates2("pbbcggttciiippooaais", 2) == "ps")
            


        