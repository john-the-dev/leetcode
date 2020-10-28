# 271. Encode and Decode Strings
'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

 

Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
'''
from common import *
'''
Encode to numbers and decode from numbers.
O(N) runtime for both encode and decode, in which N is total # of characters in strs. O(N) storage.
Beat 5% runtime, 29% storage of all Leetcode submissions.
'''
class Codec:
    def toNum(self, s):
        num,zero,i,n = 0,0,0,len(s)
        while i < n and ord(s[i]) == 0:
            zero += 1
            i += 1
        while i < n:
            num = num << 8
            num += ord(s[i])
            i += 1
        return [zero,num]

    def toStr(self, zero, num):
        s = []
        while num > 0:
            s.append(chr(num % 256))
            num = num >> 8
        s.extend([chr(0)]*zero)
        return ''.join(s[::-1])

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        out = []
        for s in strs:
            zero,num = self.toNum(s)
            out.append('{}:{}'.format(zero,num))
        return ','.join(out)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        out = []
        strs = s.split(',') if len(s) > 0 else []
        for s in strs:
            zero,num = s.split(':')
            out.append(self.toStr(int(zero),int(num)))
        return out

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Tests.
codec = Codec()
strs = ['Great','Nice']
encoded = codec.encode(strs)
assert(codec.decode(encoded) == strs)
strs = ['{}leading'.format(chr(0)),'Nice']
encoded = codec.encode(strs)
assert(codec.decode(encoded) == strs)
strs = ['{}l:eadi.ng'.format(chr(0)),'{}leading,{}'.format(chr(0),chr(1))]
encoded = codec.encode(strs)
assert(codec.decode(encoded) == strs)
strs = []
encoded = codec.encode(strs)
assert(codec.decode(encoded) == strs)
