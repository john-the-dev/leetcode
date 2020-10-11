from typing import List  # This ensures the compile can accept Leetcode Python 3 syntax: https://leetcode.com/discuss/general-discussion/270755/in-python-3-the-parameter-type-define-list-always-reports-an-error-in-ide

# Check if two lists carry same items without considering the order of the items.
def assert_list_noorder(list1, list2):
    list1.sort()
    list2.sort()
    assert(list1 == list2)

# Assert a sequence of calls return expected results.
def assert_call_sequence(context, calls, args, expected_outputs):
    assert(len(calls) == len(args) == len(expected_outputs[0]))
    assert(len(calls) >= 1)
    output = []
    # Default first item in calls is to create the class object of the solution and the remaining is to call methods of the object.
    solution = context[calls[0]](*args[0])
    output.append(None)
    for i in range(1,len(calls)):
        call = getattr(solution, calls[i])
        output.append(call(*args[i]))
    assert(output in expected_outputs)

class NestedInteger:
    def __init__(self, item):
        if isinstance(item, int):
            self.type = 0
            self.val = item
        else:
            self.type = 1
            self.val = []
            for i in item:
                self.val.append(NestedInteger(i))

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.type == 0

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val if self.type == 0 else None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.val if self.type == 1 else None

class DSU:
    def __init__(self):
        self.graph = {}
    def find(self, id):
        if id not in self.graph:
            self.graph[id] = id
        elif self.graph[id] != id:
            self.graph[id] = self.find(self.graph[id])
        return self.graph[id]
    def union(self, id1, id2):
        self.graph[self.find(id2)] = self.find(id1)
    