# 468. Validate IP Address
'''
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
Example 4:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
Output: "Neither"
Example 5:

Input: IP = "1e1.4.5.6"
Output: "Neither"
 

Constraints:

IP consists only of English letters, digits and the characters '.' and ':'.
'''
from common import *
class Solution:
    '''
    Parsing rules.
    O(n) runtime, O(n) storage, in which n is length of the IP.
    Beat 45% runtime, 29% storage of all Leetcode submissions.
    '''
    def validIPAddress(self, IP: str) -> str:
        if IP.find('.') > 0:
            parts = IP.split('.')
            if len(parts) != 4: return 'Neither'
            for part in parts:
                if (not part.isdigit()) or (len(part) > 3) or (len(part) > 1 and part[0] == '0') or (int(part) >= 256): return 'Neither'
            return 'IPv4'
        elif IP.find(':') > 0:
            parts = IP.split(':')
            if len(parts) != 8: return 'Neither'
            for part in parts:
                if len(part) == 0 or len(part) > 4: return 'Neither'
                for c in part:
                    if c >= 'a' and c <= 'f': continue
                    if c >= 'A' and c <= 'F': continue
                    if c >= '0' and c <= '9': continue
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'

    '''
    Improve storage complexity by counting occurence of the delimiter before spliting.
    O(n) runtime, O(1) storage.
    Beat 77% runtime, 9% storage of all Leetcode submissions.
    Note by counting the delimiter occurence, we make sure there are constant # of parts for IPv4 and IPv6 check. So storage is O(1).
    '''
    def validIPAddress2(self, IP: str) -> str:
        if IP.count('.') == 3:
            parts = IP.split('.')
            if len(parts) != 4: return 'Neither'
            for part in parts:
                if (not part.isdigit()) or (len(part) > 3) or (len(part) > 1 and part[0] == '0') or (int(part) >= 256): return 'Neither'
            return 'IPv4'
        elif IP.count(':') == 7:
            parts = IP.split(':')
            if len(parts) != 8: return 'Neither'
            for part in parts:
                if len(part) == 0 or len(part) > 4: return 'Neither'
                for c in part:
                    if c >= 'a' and c <= 'f': continue
                    if c >= 'A' and c <= 'F': continue
                    if c >= '0' and c <= '9': continue
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'

# Tests.
assert(Solution().validIPAddress("172.16.254.1") == 'IPv4')
assert(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == 'IPv6')
assert(Solution().validIPAddress("256.256.256.256") == 'Neither')
assert(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:") == 'Neither')
assert(Solution().validIPAddress("1e1.4.5.6") == 'Neither')
assert(Solution().validIPAddress2("172.16.254.1") == 'IPv4')
assert(Solution().validIPAddress2("2001:0db8:85a3:0:0:8A2E:0370:7334") == 'IPv6')
assert(Solution().validIPAddress2("256.256.256.256") == 'Neither')
assert(Solution().validIPAddress2("2001:0db8:85a3:0:0:8A2E:0370:7334:") == 'Neither')
assert(Solution().validIPAddress2("1e1.4.5.6") == 'Neither')
                
