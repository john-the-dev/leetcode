# 1166. Design File System
'''
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

The number of calls to the two functions is less than or equal to 104 in total.
2 <= path.length <= 100
1 <= value <= 109
'''
from common import *
class Item:
    def __init__(self, val):
        self.val = val
        self.subs = {}
class FileSystem:

    '''
    A directory tree with hash map to allow quick locate file/path item.
    O(n) runtime for both createPath and get, O(N) storage in which N is all different path items added and n is the length of a specific path.
    Beat 66% runtime, 9% storage of all Leetcode submissions.
    '''
    def __init__(self):
        self.root = Item(None)

    def createPath(self, path: str, value: int) -> bool:
        subs = path.split('/')
        item = self.root
        for i in range(1,len(subs)-1):
            if subs[i] not in item.subs: return False
            item = item.subs[subs[i]]
        if subs[-1] in item.subs: return False
        item.subs[subs[-1]] = Item(value)
        return True

    def get(self, path: str) -> int:
        subs = path.split('/')
        item = self.root
        for i in range(1,len(subs)):
            if subs[i] not in item.subs: return -1
            item = item.subs[subs[i]]
        return item.val

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Tests.
assert_call_sequence(globals(),["FileSystem","createPath","get"],[[],["/a",1],["/a"]],[[None,True,1]])
assert_call_sequence(globals(),["FileSystem","createPath","createPath","get","createPath","get"],[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]],[[None,True,True,2,False,-1]])
