# 160. Intersection of Two Linked Lists
'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.    
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from common import *
class Solution:
    '''
    Align the linked lists then compare side by side.
    O(m+n) runtime, O(1) storage.
    Beat 59% runtime, 11% storage of all Leetcode submissions.
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLen(head):
            l = 0
            while head != None:
                head = head.next
                l += 1
            return l
        lenA,lenB = getLen(headA),getLen(headB)
        if lenA < lenB: lenA,lenB,headA,headB = lenB,lenA,headB,headA
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while headA != None and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
    
# Tests.
headA = createLinkedListFromArray([4,1,8,4,5])
headB = createLinkedListFromArray([5,6,1])
headB.next.next.next = headA.next.next
assert(Solution().getIntersectionNode(headA,headB) == headA.next.next)
headA = createLinkedListFromArray([1,9,1,2,4])
headB = createLinkedListFromArray([3])
headB.next = headA.next.next.next
assert(Solution().getIntersectionNode(headA,headB) == headA.next.next.next)
headA = createLinkedListFromArray([2,6,4])
headB = createLinkedListFromArray([1,5])
assert(Solution().getIntersectionNode(headA,headB) == None)
