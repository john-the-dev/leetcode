# 706. Design HashMap
'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
'''
from common import *
class HashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = [[] for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % len(self.h)
        for j in range(len(self.h[i])):
            if self.h[i][j][0] == key:
                self.h[i][j][1] = value
                return
        self.h[i].append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % len(self.h)
        for j in range(len(self.h[i])):
            if self.h[i][j][0] == key: return self.h[i][j][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % len(self.h)
        n = len(self.h[i])
        for j in range(n):
            if self.h[i][j][0] == key:
                if j < n-1: self.h[i][j],self.h[i][n-1] = self.h[i][n-1],self.h[i][j]
                self.h[i].pop()
                break

assert_call_sequence(globals(),["HashMap","put","put","get","get","put","get", "remove", "get"],[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]],[[None,None,None,1,-1,None,1,None,-1]])