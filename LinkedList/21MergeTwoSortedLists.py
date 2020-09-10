# 21. Merge Two Sorted Lists
'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *
class Solution:
    '''
    Solution: track the two lists and append the smaller val to the result list every time.
    '''
    def mergeTwoLists(self, l1, l2):
        r,curr = None,None
        def append(l):
            nonlocal curr,r
            if curr == None:
                curr = ListNode(l.val)
                r = curr
            else:
                curr.next = ListNode(l.val)
                curr = curr.next
            return l.next
        while l1 != None or l2 != None:
            if l1 == None:
                l2 = append(l2)
            elif l2 == None:
                l1 = append(l1)
            elif l1.val < l2.val:
                l1 = append(l1)
            else:
                l2 = append(l2)
        return r

# Tests
assert(createArrayFromLinkedList(Solution().mergeTwoLists(createLinkedListFromArray([1,2,4]), createLinkedListFromArray([1,3,4]))) == [1,1,2,3,4,4])
assert(createArrayFromLinkedList(Solution().mergeTwoLists(createLinkedListFromArray([]), createLinkedListFromArray([1,3,4]))) == [1,3,4])
assert(createArrayFromLinkedList(Solution().mergeTwoLists(createLinkedListFromArray([]), createLinkedListFromArray([]))) == [])

