# 143. Reorder List
'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *
class Solution:
    '''
    Reverse second half of the linked list and then merge the two lists.
    O(n) runtime, O(1) storage.
    Beat 60% runtime, 5% storage of all Leetcode submissions.
    '''
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node,n = head,0
        while node != None:
            n += 1
            node = node.next
        prev,half,m = None,head,n//2 if n % 2 == 0 else n//2+1
        while m > 0:
            m -= 1
            prev = half
            half = half.next
        if prev != None: prev.next = None
        prev,curr = None,half
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        node,node2,node1,first = head,prev,head.next if head != None else None,False
        while node1 != None or node2 != None:
            if first:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            first,node = not first,node.next

# Tests.
head = createLinkedListFromArray([1,2,3,4])
Solution().reorderList(head)
assert(createArrayFromLinkedList(head) == [1,4,2,3])
head = createLinkedListFromArray([1,2,3,4,5])
Solution().reorderList(head)
assert(createArrayFromLinkedList(head) == [1,5,2,4,3])
head = createLinkedListFromArray([])
Solution().reorderList(head)
assert(createArrayFromLinkedList(head) == [])
head = createLinkedListFromArray([1])
Solution().reorderList(head)
assert(createArrayFromLinkedList(head) == [1])
head = createLinkedListFromArray([1,2])
Solution().reorderList(head)
assert(createArrayFromLinkedList(head) == [1,2])
