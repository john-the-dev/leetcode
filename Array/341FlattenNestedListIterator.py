# 341. Flatten Nested List Iterator
'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from common import *
class NestedIterator:
    '''
    Stack based approach to simulate pausable recursion so that we can iterate. Note recursion itself does not work because it cannot pause.
    O(n) for whole iteration, O(d) stoage, in which n is total # of items in NestedInteger and d is depth of the nested structure.
    Beat 90% runtime, 23% storage of all Leetcode submissions.
    '''
    def __init__(self, nestedList):
        self.stack = []
        self.goNext(nestedList, -1)
    
    def goNext(self, nestedList, i):
        i += 1
        while self.stack and i == len(nestedList):
            nestedList,i = self.stack.pop()
            i += 1
        while i < len(nestedList):
            self.stack.append((nestedList,i))
            if nestedList[i].isInteger(): break
            nestedList,i = nestedList[i].getList(),0

    def next(self):
        nestedList,i = self.stack.pop()
        out = nestedList[i].getInteger()
        self.goNext(nestedList, i)
        return out
    
    def hasNext(self) -> bool:
        while self.stack and (not self.stack[-1][0][self.stack[-1][1]].isInteger()):
            nestedList,i = self.stack.pop()
            self.goNext(nestedList, i)
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Tests.
nested = NestedInteger([[1,1],2,[1,1]])
i, v = NestedIterator(nested.getList()), []
while i.hasNext(): v.append(i.next())
assert(v == [1,1,2,1,1])
nested = NestedInteger([1,[4,[6]]])
i, v = NestedIterator(nested.getList()), []
while i.hasNext(): v.append(i.next())
assert(v == [1,4,6])
nested = NestedInteger([[1,1],[[2]],[1,1]])
i, v = NestedIterator(nested.getList()), []
while i.hasNext(): v.append(i.next())
assert(v == [1,1,2,1,1])
nested = NestedInteger([1,2,3])
i, v = NestedIterator(nested.getList()), []
while i.hasNext(): v.append(i.next())
assert(v == [1,2,3])
nested = NestedInteger([[]])
i, v = NestedIterator(nested.getList()), []
while i.hasNext(): v.append(i.next())
assert(v == [])

