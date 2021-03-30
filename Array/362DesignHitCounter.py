# 362. Design Hit Counter
'''
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
 

Constraints:

1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.
 

Follow up: What if the number of hits per second could be huge? Does your design scale?
'''
from common import *
'''
list, binary search on timestamp.
O(1) runtime for init, hit, O(log(n)) runtime for getHits. O(n) storage in which n is # of seconds with hits.
Beat 85% runtime, 50% storage of all Leetcode submissions.
'''
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.arr and self.arr[-1][0] == timestamp:
            self.arr[-1][1] += 1
        else:
            self.arr.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        def binarySearch(timestamp, leftOrRight = True):
            i,j = 0,len(self.arr)
            while i < j:
                k = (i+j) // 2
                if leftOrRight:
                    if self.arr[k][0] < timestamp:
                        i = k+1
                    else:
                        j = k
                else:
                    if self.arr[k][0] <= timestamp:
                        i = k+1
                    else:
                        j = k
            return i
        j = binarySearch(timestamp, False)
        i = binarySearch(timestamp-299, True)
        out = 0
        for k in range(i, j):
            out += self.arr[k][1]
        return out

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
assert_call_sequence(globals(),["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"],[[],[1],[2],[2],[4],[300],[300],[301]],[[None,None,None,None,3,None,4,3]])