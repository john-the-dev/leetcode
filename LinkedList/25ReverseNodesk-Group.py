# 25. Reverse Nodes in k-Group
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *
class Solution:
    '''
    Record prev,curr,curr_head,curr_tail, reverse k node each time.
    O(n) runtime, O(1) storage.
    Beat 50% runtime, 49% storage of all Leetcode submissions.
    '''
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        out,curr,n = None,head,0
        while curr != None:
            n += 1
            curr = curr.next
        s,curr,prev,prev_tail = n // k,head,None,None
        while s > 0:
            curr_tail,curr_head = curr,None
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev,curr,curr_head = curr,temp,curr
            if prev_tail != None: prev_tail.next = curr_head
            if out == None: out = curr_head
            prev_tail,prev,s = curr_tail,None,s-1
        prev_tail.next = curr
        return out

# Tests.
assert(createArrayFromLinkedList(Solution().reverseKGroup(createLinkedListFromArray([1,2,3,4,5]), 2)) == [2,1,4,3,5])
assert(createArrayFromLinkedList(Solution().reverseKGroup(createLinkedListFromArray([1,2,3,4,5]), 3)) == [3,2,1,4,5])
assert(createArrayFromLinkedList(Solution().reverseKGroup(createLinkedListFromArray([1,2,3,4,5]), 1)) == [1,2,3,4,5])
assert(createArrayFromLinkedList(Solution().reverseKGroup(createLinkedListFromArray([1,2,3,4,5]), 5)) == [5,4,3,2,1])
