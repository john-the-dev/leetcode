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

