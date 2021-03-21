# Reordered Power of 2

'''

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true
 

Note:

1 <= N <= 10^9
'''
class Solution:
    '''
    Frequency table based signature.
    O(n) runtime, O(1) storage.
    33 min.
    '''
    def reorderedPowerOf2(self, N: int) -> bool:
        def sig(n):
            h = [0]*10
            while n > 0:
                d = n % 10
                n = n // 10
                h[d] += 1
            return h
        h = sig(N)
        high = 0
        for i in range(len(h)-1,-1,-1):
            if h[i] > 0:
                j = h[i]
                while j > 0:
                    high += high*10+i
                    j -= 1
        c = 1
        while c <= high:
            if sig(c) == h: return True
            c = 2*c
        return False

# Tests.
assert(Solution().reorderedPowerOf2(1) == True)
assert(Solution().reorderedPowerOf2(10) == False)
assert(Solution().reorderedPowerOf2(16) == True)
assert(Solution().reorderedPowerOf2(24) == False)
assert(Solution().reorderedPowerOf2(46) == True)


        


