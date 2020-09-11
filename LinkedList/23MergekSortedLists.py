# 23. Merge k Sorted Lists
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *
import heapq
class Solution:
    '''
    Priority queue based approach.
    O(Nlog(k)) runtime, in which k is # of lists and N is total # of items. O(k) storage as priority queue has k items.
    Beat 84% runtime, 59% storage.
    '''
    def mergeKLists(self, lists):
        q = []
        for i,l in enumerate(lists):
            if l != None: q.append([l.val,i])
        heapq.heapify(q)
        out,curr,prev = None,None,None
        while q:
            v,i = heapq.heappop(q)
            if out == None:
                out = lists[i]
                curr = out
            else:
                prev = curr
                curr = lists[i]
                prev.next = curr
            temp,lists[i].next = lists[i].next,None
            lists[i] = temp
            if lists[i] != None: heapq.heappush(q, [lists[i].val,i])
        return out

    '''
    Divide and conquer based approach to improve on storage. Note we have to use loop instead of recursion for divide conquer as recursion requires O(log(k)) storage on call stack while loop and reusing lists reduces storage to O(1).
    O(Nlog(k)) runtime, O(1) storage.
    Beat 41% runtime, 77% storage.
    '''
    def mergeKLists2(self, lists):
        def merge2Lists(list1, list2):
            root,curr = None,None
            def append(l):
                nonlocal root,curr
                r = l.next
                if curr == None:
                    curr = l
                    root = curr
                else:
                    curr.next = l
                    curr = curr.next
                l.next = None
                return r
            while list1 != None or list2 != None:
                if list1 == None:
                    list2 = append(list2)
                elif list2 == None:
                    list1 = append(list1)
                elif list1.val < list2.val:
                    list1 = append(list1)
                else:
                    list2 = append(list2)
            return root
        k = len(lists)
        while k > 1:
            i = 0
            while 2*i < k:
                if 2*i == k-1:
                    lists[i] = lists[i*2]
                else:
                    lists[i] = merge2Lists(lists[2*i], lists[2*i+1])
                i += 1
            k = k // 2 if k % 2 == 0 else k // 2 + 1
        return lists[0] if lists else None

assert(createArrayFromLinkedList(Solution().mergeKLists([createLinkedListFromArray([1,4,5]),createLinkedListFromArray([1,3,4]),createLinkedListFromArray([2,6])])) == [1,1,2,3,4,4,5,6])
assert(createArrayFromLinkedList(Solution().mergeKLists([])) == [])
assert(createArrayFromLinkedList(Solution().mergeKLists([createLinkedListFromArray([])])) == [])
assert(createArrayFromLinkedList(Solution().mergeKLists2([createLinkedListFromArray([1,4,5]),createLinkedListFromArray([1,3,4]),createLinkedListFromArray([2,6])])) == [1,1,2,3,4,4,5,6])
assert(createArrayFromLinkedList(Solution().mergeKLists2([])) == [])
assert(createArrayFromLinkedList(Solution().mergeKLists2([createLinkedListFromArray([])])) == [])