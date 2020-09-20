# 460. LFU Cache
'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
from common import *
import sys
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2meta = {}
        self.freq2meta = {}
        self.low_freq = sys.maxsize

    def update(self, key: int) -> int:
        freq,node = self.key2meta[key]
        if freq in self.freq2meta:
            if node.prev != None: node.prev.next = node.next
            if node.next != None: node.next.prev = node.prev
            if self.freq2meta[freq][0] == node: self.freq2meta[freq][0] = node.next
            if self.freq2meta[freq][1] == node: self.freq2meta[freq][1] = node.prev
            if self.freq2meta[freq][0] == None: 
                del self.freq2meta[freq]
                if self.low_freq == freq: self.low_freq = sys.maxsize
            node.next,node.prev = None,None
        new_freq = freq + 1
        if new_freq not in self.freq2meta: self.freq2meta[new_freq] = [None,None]
        if self.freq2meta[new_freq][0] == None:
            self.freq2meta[new_freq][0],self.freq2meta[new_freq][1] = node,node
        else:
            node.next,node.prev = self.freq2meta[new_freq][0],None
            self.freq2meta[new_freq][0].prev = node
            self.freq2meta[new_freq][0] = node
        self.key2meta[key][0] = new_freq
        self.low_freq = min(self.low_freq,new_freq)
        
    def get(self, key: int) -> int:
        if key not in self.key2meta: return -1
        self.update(key)
        return self.key2meta[key][1].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key2meta:
            self.key2meta[key][1].val = value
            self.update(key)
        else:
            if len(self.key2meta) == self.capacity:
                head,tail = self.freq2meta[self.low_freq]
                if head == tail:
                    del self.key2meta[head.key]
                    del self.freq2meta[self.low_freq]
                    self.low_freq = sys.maxsize
                else:
                    self.freq2meta[self.low_freq][1] = tail.prev
                    tail.prev.next = None
                    del self.key2meta[tail.key]
            node = Node(key, value)
            self.key2meta[key] = [0,node]
            self.update(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Tests.
assert_call_sequence(globals(),["LFUCache","put","put","get","put","get","get","put","get","get","get"],[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]],[[None,None,None,1,None,-1,3,None,-1,3,4]])