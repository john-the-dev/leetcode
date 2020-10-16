# 622. Design Circular Queue
'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
'''
class MyCircularQueue:

    '''
    Two pointers (rear and front) and update status when enQueue and deQueue. Rear always points to the first available location and Front always points to the front element of the queue. If they are the same, it is either full or empty.
    O(1) runtime for all calls except __init__ which is O(n). O(n) storage.
    Beat 99% runtime, 27% storage of all Leetcode submissions.
    '''
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None]*k
        self.k = k
        self.front,self.rear,self.full = 0,0,False

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.queue[self.rear] = value
        self.rear += 1
        if self.rear == self.k: self.rear = 0
        if self.front == self.rear: self.full = True
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.front += 1
        if self.front == self.k: self.front = 0
        self.full = False
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        i = self.rear-1 if self.rear > 0 else self.k-1
        return self.queue[i]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return (not self.full) and (self.front == self.rear)

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Tests.
circularQueue = MyCircularQueue(3)
assert(circularQueue.enQueue(1) == True)
assert(circularQueue.enQueue(2) == True)
assert(circularQueue.enQueue(3) == True)
assert(circularQueue.enQueue(4) == False)
assert(circularQueue.Rear() == 3)
assert(circularQueue.isFull() == True)
assert(circularQueue.deQueue() == True)
assert(circularQueue.enQueue(4) == True)
assert(circularQueue.Rear() == 4)