# 86. Partition List
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *
class Solution:
    '''
    Look through the linked list, create two list (1 before and 1 after), then combine the two lists.
    O(n) runtime, O(1) storage.
    Beat 57% runtime, 19% storage of all Leetcode submissions.
    '''
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1,head2,curr1,curr2,curr = None,None,None,None,head
        while curr != None:
            if curr.val < x:
                if head1 == None:
                    head1,curr1 = curr,curr
                else:
                    curr1.next,curr1 = curr,curr
            else:
                if head2 == None:
                    head2,curr2 = curr,curr
                else:
                    curr2.next,curr2 = curr,curr
            curr = curr.next
        if curr2 != None: curr2.next = None
        if curr1 != None: curr1.next = head2
        return head1 if curr1 != None else head2

# Tests.
assert(createArrayFromLinkedList(Solution().partition(createLinkedListFromArray([1,4,3,2,5,2]),3)) == [1,2,2,4,3,5])
assert(createArrayFromLinkedList(Solution().partition(createLinkedListFromArray([1,2,2]),3)) == [1,2,2])
assert(createArrayFromLinkedList(Solution().partition(createLinkedListFromArray([4,3,5]),3)) == [4,3,5])
        
