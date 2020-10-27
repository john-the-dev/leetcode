# 204. Count Primes
'''
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
'''
from common import *
class Solution:
    '''
    Simplified version of Sieve of Eratosthenes: find all non primes and block them when counting bigger numbers.
    O(kn/2) runtime, O(n-k) storage, in which k is # of primes less than n.
    Beat 17% runtime, 5% storage of all Leetcode submissions.
    '''
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        primes,nonePrimes = 0,set()
        p = 2
        while p < n:
            k = 2*p
            while k <= n:
                nonePrimes.add(k)
                k += p
            primes += 1
            p += 1
            while p in nonePrimes:
                p += 1
        return primes

    '''
    Optimized version of Sieve of Eratosthenes: stop at n^0.5 for p.
    O(kn^0.5) runtime, O(n-k) storage.
    Beat 28% runtime, 5% storage of all Leetcode submissions.
    '''
    def countPrimes2(self, n: int) -> int:
        if n < 2: return 0
        primes,nonePrimes = 0,set()
        p = 2
        while p*p < n:
            k = p*p
            while k <= n:
                nonePrimes.add(k)
                k += p
            primes += 1
            p += 1
            while p in nonePrimes:
                p += 1
        for i in range(p,n):
            if i not in nonePrimes: primes += 1
        return primes

# Tests.
assert(Solution().countPrimes(2) == 0)
assert(Solution().countPrimes(4) == 2)  
assert(Solution().countPrimes(10) == 4)
assert(Solution().countPrimes(0) == 0)
assert(Solution().countPrimes(1) == 0)
assert(Solution().countPrimes2(2) == 0)
assert(Solution().countPrimes2(4) == 2)  
assert(Solution().countPrimes2(10) == 4)
assert(Solution().countPrimes2(0) == 0)
assert(Solution().countPrimes2(1) == 0)  
    
