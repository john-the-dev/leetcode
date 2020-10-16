# 751. IP to CIDR
'''
Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list (of smallest possible length) of CIDR blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length. For example: "123.45.67.89/20". That prefix length "20" represents the number of common prefix bits in the specified range.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just this one address.

The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just 11111111 00000000 00000000 00010000.

In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .

There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.

Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100 
that are outside the specified range.
Note:
ip will be a valid IPv4 address.
Every implied address ip + x (for x < n) will be a valid IPv4 address.
n will be an integer in the range [1, 1000].
'''
from common import *
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        segments,out,val = ip.split('.'),[],0
        for i in range(4):
            val = val << 8
            val += int(segments[i])
        def toString(val,b):
            segments = []
            while len(segments) < 4:
                segments.append(str(val % 256))
                val = val >> 8
            return '{}/{}'.format('.'.join(segments[::-1]),32-b)
        b,i = 0,1
        while n >= i:
            if val & i or (i << 1) > n:
                out.append(toString(val,b))
                val = val + i
                n -= i
                b,i = 0,1
            else:
                b += 1
                i = i << 1
        return out

# Tests.
assert(Solution().ipToCIDR("255.0.0.7", 10) == ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"])
assert(Solution().ipToCIDR("0.0.0.0", 10) == ["0.0.0.0/29","0.0.0.8/31"])
assert(Solution().ipToCIDR("0.0.0.0", 2) == ["0.0.0.0/31"]) # https://leetcode.com/problems/ip-to-cidr/discuss/847445/Test-Case-%22%220.0.0.0%22-2-is-WRONG.-Answer-should-be-%220.0.0.031%22

        
        