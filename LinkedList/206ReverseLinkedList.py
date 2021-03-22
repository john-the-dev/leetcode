# 206. Reverse Linked List
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *
class Solution:
    '''
    Iterative approach.
    O(n) runtime, O(1) storage.
    Beat 69% runtime, 94% storage of all Leetcode submissions.
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        prev,curr = None,head
        while curr != None:
            temp = curr.next
            curr.next = prev
            curr,prev = temp,curr
        return prev

    '''
    Recursive approach.
    O(n) runtime, O(n) storage due to using call stack.
    '''
    def reverseList2(self, head: ListNode) -> ListNode:
        tail = None
        def reverse(curr, prev):
            nonlocal tail
            if curr == None:
                tail = prev
                return
            temp = curr.next
            curr.next = prev
            reverse(temp,curr)
        reverse(head, None)
        return tail

# Tests.
assert(createArrayFromLinkedList(Solution().reverseList(createLinkedListFromArray([1,2,3,4,5]))) == [5,4,3,2,1])
assert(createArrayFromLinkedList(Solution().reverseList(createLinkedListFromArray([1,2]))) == [2,1])
assert(createArrayFromLinkedList(Solution().reverseList(createLinkedListFromArray([]))) == [])
assert(createArrayFromLinkedList(Solution().reverseList2(createLinkedListFromArray([1,2,3,4,5]))) == [5,4,3,2,1])
assert(createArrayFromLinkedList(Solution().reverseList2(createLinkedListFromArray([1,2]))) == [2,1])
assert(createArrayFromLinkedList(Solution().reverseList2(createLinkedListFromArray([]))) == [])