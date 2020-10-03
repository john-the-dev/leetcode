# 5. Longest Palindromic Substring
'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''
class Solution:
    '''
    Loop and expand from there to find longest palindrome.
    O(n^2) runtime, O(1) storage.
    Beat 63% runtime, 25% storage of all Leetcode submissions.
    '''
    def longestPalindrome(self, s):
        n,out = len(s),[0,-1]
        for i in range(n):
            j,k = i,i
            while j >= 0 and k < n and s[j] == s[k]:
                if k-j > out[1]-out[0]: out = [j,k]
                j -= 1
                k += 1
            j,k = i,i+1
            while j >= 0 and k < n and s[j] == s[k]:
                if k-j > out[1]-out[0]: out = [j,k]
                j -= 1
                k += 1
        return s[out[0]:out[1]+1]

# Tests.
assert(Solution().longestPalindrome("babad") == "bab")
assert(Solution().longestPalindrome("cbbd") == "bb")
assert(Solution().longestPalindrome("a") == "a")
assert(Solution().longestPalindrome("") == "")
