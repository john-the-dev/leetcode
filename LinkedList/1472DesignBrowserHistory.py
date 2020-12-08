# 1472. Design Browser History
'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
'''
from common import *
'''
Linked list which allows to back and forward easily.
O(1) runtime for init, visit, O(k) runtime for back and forward, O(n) storage for BrowserHistory class.
Beat 5% runtime, 6% storage of all Leetcode submissions. 
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        self.head = self.curr

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.curr.prev == None: break
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr.next == None: break
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

'''
Array based implmentation. It saves runtime for back and forward.
O(1) runtime for init, back, and forward, O(n) runtime for visit as we slice, in which n is # of elements in history. O(n) storage for BrowserHistory.
Beat 49% runtime, 55% storage of all Leetcode submissions.
'''
class BrowserHistory2:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.curr+1]
        self.arr.append(url)
        self.curr = len(self.arr)-1

    def back(self, steps: int) -> str:
        self.curr = 0 if self.curr < steps else self.curr-steps
        return self.arr[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = len(self.arr)-1 if self.curr+steps >= len(self.arr) else self.curr+steps
        return self.arr[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Tests.
assert_call_sequence(globals(),["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"],
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]],[[None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"]])
assert_call_sequence(globals(),["BrowserHistory2","visit","visit","visit","back","back","forward","visit","forward","back","back"],
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]],[[None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"]])