# 3. Longest Substring Without Repeating Characters
'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    '''
    Classic sliding window approach.
    O(n) runtime, O(n) storage.
    '''
    def lengthOfLongestSubstring(self, s):
        i,j,n,seen,out = 0,0,len(s),set(),0
        while j < n:
            while j < n and s[j] not in seen:
                seen.add(s[j])
                j += 1
            out = max(j-i, out)
            if j < n:
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                i += 1
                j += 1
        return out

# Tests.
assert(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
assert(Solution().lengthOfLongestSubstring("bbbbb") == 1)
assert(Solution().lengthOfLongestSubstring("pwwkew") == 3)
assert(Solution().lengthOfLongestSubstring("bacabcbb") == 3)
