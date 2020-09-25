# 981. Time Based Key-Value Store
'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
'''
'''
Use array to store value and timestamp, then use binary search to locate the timestamp_prev.
O(1) runtime for set, O(log(n)) runtime for get, O(n) storage.
Beat 60% runtime, 9% storage of all Leetcode submissions.
'''
from common import *
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def set(self, key, value, timestamp):
        if key not in self.map: self.map[key] = []
        self.map[key].append([timestamp,value])

    def get(self, key, timestamp):
        if key not in self.map: return ''
        b,e = 0,len(self.map[key])
        while b < e:
            k = (b+e)//2
            prev = self.map[key][k][0]
            if prev == timestamp:
                return self.map[key][k][1]
            elif prev < timestamp:
                b = k+1
            else:
                e = k
        return '' if b == 0 else self.map[key][b-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Tests.
assert_call_sequence(globals(), ["TimeMap","set","get","get","set","get","get"], [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]], [[None,None,"bar","bar",None,"bar2","bar2"]])
assert_call_sequence(globals(), ["TimeMap","set","set","get","get","get","get","get"], [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]], [[None,None,None,"","high","high","low","low"]])