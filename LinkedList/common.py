from typing import List  # This ensures the compile can accept Leetcode Python 3 syntax: https://leetcode.com/discuss/general-discussion/270755/in-python-3-the-parameter-type-define-list-always-reports-an-error-in-ide

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def createLinkedListFromArray(arr):
    out,curr = None,None
    for val in arr:
        if curr == None:
            curr = ListNode(val)
            out = curr
        else:
            curr.next = ListNode(val)
            curr = curr.next
    return out

def createArrayFromLinkedList(head):
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next
    return arr

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

