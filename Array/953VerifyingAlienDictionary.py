# 953. Verifying an Alien Dictionary
'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''
from common import *
class Solution:
    '''
    Hash map (key is char and value is position in order) to allow for quick compare (O(1)) of order.
    O(nm) runtime, O(k) storage, in which n is length of words and m is length of each word.
    Beat 69% runtime, 79% storage of all Leetcode submissions.
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {None:-1}
        for i,c in enumerate(order):
            h[c] = i
        for i in range(1,len(words)):
            word0,word1 = words[i-1],words[i]
            s0,s1 = len(word0),len(word1)
            for j in range(max(s0,s1)):
                p0,p1 = h[word0[j]] if j < s0 else h[None],h[word1[j]] if j < s1 else h[None]
                if p0 > p1: return False
                if p0 < p1: break
        return True

# Tests.
assert(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True)
assert(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False)
assert(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False)
assert(Solution().isAlienSorted(["app","apple"], "abcdefghijklmnopqrstuvwxyz") == True)
assert(Solution().isAlienSorted(["hello","leetcode","leet"], "hlabcdefgijkmnopqrstuvwxyz") == False)
assert(Solution().isAlienSorted(["kuvp","q"],"ngxlkthsjuoqcpavbfdermiywz") == True)