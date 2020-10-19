# 295. Find Median from Data Stream
'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''
from common import *
import heapq
class MedianFinder:

    '''
    Two priority queue (1 max queue and 1 min queue).
    O(log(n)) for addNum, O(1) for findMedian, O(n) storage for the class.
    Beat 95% runtime, 12% storage.
    For scenario in which most data are between 0 and 100, we can add a count to each item in priority queue and update the queues accordingly so to reduce storage use.
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left,self.right = [],[]

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right):
            if num >= -self.left[0]:
                heapq.heappush(self.right,num)
            else:
                heapq.heappush(self.right,-heapq.heappop(self.left))
                heapq.heappush(self.left,-num)
        elif self.right:
            if num <= self.right[0]:
                heapq.heappush(self.left,-num)
            else:
                heapq.heappush(self.left,-heapq.heappop(self.right))
                heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left,-num)

    def findMedian(self) -> float:
        return -self.left[0] if len(self.left) > len(self.right) else (-self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Tests.
assert_call_sequence(globals(),['MedianFinder','addNum','addNum','findMedian','addNum','findMedian','addNum','findMedian','addNum','findMedian'],[[],[1],[2],[],[3],[],[1],[],[1],[]],[[None,None,None,1.5,None,2,None,1.5,None,1]])