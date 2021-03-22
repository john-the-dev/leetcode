# 2. Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from common import *
class Solution:
    '''
    Loop through two linked lists, add accordingly, generate resulting linked list.
    O(1) storage, O(max(m,n)) runtime.
    Beat 89% runtime, 13% storage of all Leetcode submissions.
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = None
        curr1,curr2,carry,curr = l1,l2,0,l
        while curr1 != None or curr2 != None:
            val1 = curr1.val if curr1 != None else 0
            val2 = curr2.val if curr2 != None else 0
            val = val1+val2+carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            if curr == None:
                l = ListNode(val)
                curr = l
            else:
                curr.next = ListNode(val)
                curr = curr.next
            if curr1 != None: curr1 = curr1.next
            if curr2 != None: curr2 = curr2.next
        if carry > 0: curr.next = ListNode(carry)
        return l

# Tests.
assert(createArrayFromLinkedList(Solution().addTwoNumbers(createLinkedListFromArray([2,4,3]),createLinkedListFromArray([5,6,4]))) == [7,0,8])
assert(createArrayFromLinkedList(Solution().addTwoNumbers(createLinkedListFromArray([0]),createLinkedListFromArray([0]))) == [0])
assert(createArrayFromLinkedList(Solution().addTwoNumbers(createLinkedListFromArray([9,9,9,9,9,9,9]),createLinkedListFromArray([9,9,9,9]))) == [8,9,9,9,0,0,0,1])

