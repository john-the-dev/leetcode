# 72. Edit Distance
'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''
class Solution:
    '''
    The classic dynamic programming problem. dp[j][i] = min(dp[j-1][i-1]+1/0),dp[j-1][i]+1,dp[j][i-1]), in which first element is about edit, second about delete, and last one about insert.
    O(mn) runtime, O(mn) storage, in which m and n are length of word1 and word2 respectively.
    Beat 63% runtime, 40% storage of all Leetcode submissions.
    '''
    def minDistance(self, word1, word2):
        n1,n2 = len(word1),len(word2)
        dp = [[0 for i in range(n1+1)] for j in range(n2+1)]
        for i in range(n1+1):
            dp[0][i] = i
        for j in range(n2+1):
            dp[j][0] = j
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                e = 0 if word1[i-1] == word2[j-1] else 1
                dp[j][i] = min(dp[j-1][i-1]+e,dp[j-1][i]+1,dp[j][i-1]+1)
        return dp[n2][n1]

# Tests.
assert(Solution().minDistance("horse", "ros") == 3)
assert(Solution().minDistance("intention", "execution") == 5)
assert(Solution().minDistance("horse", "") == 5)
assert(Solution().minDistance("", "ros") == 3)
