# 273. Integer to English Words
'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1
'''
from common import *
class Solution:
    '''
    Rule: suffix for each 3 digit, custom value for digits less than 20.
    O(n) runtime, O(1) storage, in which n is # of digits in the number.
    Beat 89% runtime, 100% storage of all Leetcode submissions.
    '''
    def numberToWords(self, num: int) -> str:
        s = str(num)
        suffix = ['','Thousand','Million','Billion']
        digit = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        Ten2Ninteen = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        second = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        n = len(s)
        def subWord(i,j):
            if int(s[i:j]) == 0: return []
            out = []
            while i < j:
                d = j-i
                if d == 3:
                    if digit[int(s[i])] != '':
                        out.append(digit[int(s[i])])
                        out.append('Hundred')
                elif d == 2:
                    if digit[int(s[i])] != '':
                        if int(s[i:j]) < 20:
                            out.append(Ten2Ninteen[int(s[i:j])-10])
                            i += 2
                            continue
                        else:
                            out.append(second[int(s[i])-2])
                else:
                    if digit[int(s[i])] != '':
                        out.append(digit[int(s[i])])
                i += 1
            return out
        out = []
        i = 0
        while i < n:
            k = 9
            while n-i <= k:
                k -= 3
            while k >= 0 and n-i >= k:
                sub = subWord(i,n-k)
                if len(sub) > 0:
                    out.extend(sub)
                    if suffix[k//3] != '': out.append(suffix[k//3])
                i = n-k
                k -= 3
        return ' '.join(out) if len(out) > 0 else 'Zero'

# Tests.
assert(Solution().numberToWords(19) == 'Nineteen')
assert(Solution().numberToWords(123) == 'One Hundred Twenty Three')
assert(Solution().numberToWords(12345) == 'Twelve Thousand Three Hundred Forty Five')
assert(Solution().numberToWords(1234567) == 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')
assert(Solution().numberToWords(1234567891) == 'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One')
            