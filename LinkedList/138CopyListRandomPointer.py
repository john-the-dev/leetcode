# 138. Copy List with Random Pointer
'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.
 

Constraints:

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is null or is pointing to some node in the linked list.
'''
from common import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    '''
    Use hashmap to remember nodes.
    O(n) runtime, O(n) storage.
    '''
    def copyRandomList(self, head: 'Node') -> 'Node':
        out,curr,prev,h = None,None,Node,{}
        node = head
        while node != None:
            h[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node != None:
            if out == None:
                out = h[node]
                curr = out
            else:
                curr = h[node]
                prev.next = curr
            if node.random != None: curr.random = h[node.random]
            prev = curr
            node = node.next
        return out
    '''
    Combine new_list.random and old_list.next to locate nodes in new_list for random.
    O(n) runtime, O(1) storage.
    Beat 86% runtime, 95% storage of all Leetcode submissions.
    '''
    def copyRandomList2(self, head: 'Node') -> 'Node':
        if head == None: return None
        new_head = Node(head.val,None,head.random)
        new_curr,curr = new_head,head
        while curr != None:
            new_curr.next = Node(curr.next.val,None,curr.next.random) if curr.next != None else None
            curr,new_curr = curr.next,new_curr.next
        new_curr,curr = new_head,head
        while curr != None:
            temp = curr.next
            curr.next = new_curr
            curr,new_curr = temp,new_curr.next
        new_curr = new_head
        while new_curr != None:
            if new_curr.random != None: new_curr.random = new_curr.random.next
            new_curr = new_curr.next
        return new_head