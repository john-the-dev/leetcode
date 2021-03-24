# 680. Valid Palindrome II
'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution:
    '''
    Check palindrome then encounter a different pair, then try remove one of them and check for palindrome.
    O(n) runtime, O(1) storage.
    Beat 42% runtime, 45% storage of all Leetcode submissions.
    '''
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(i,j):
            while i < j:
                if s[i] != s[j]: return [i,j]
                i += 1
                j -= 1
            return [-1,-1]
        i,j = checkPalindrome(0,len(s)-1)
        if i != -1 and checkPalindrome(i+1,j) == [-1,-1]: return True
        if j != -1 and checkPalindrome(i,j-1) == [-1,-1]: return True
        return i == -1 and j == -1

# Tests.
assert(Solution().validPalindrome("aba") == True)
assert(Solution().validPalindrome("abca") == True)
assert(Solution().validPalindrome("a") == True)
assert(Solution().validPalindrome("abcca") == True)
assert(Solution().validPalindrome("abbca") == True)
assert(Solution().validPalindrome("abdca") == False)