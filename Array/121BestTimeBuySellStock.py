# 121. Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
from common import *
class Solution:
    '''
    Memorizing lowest price and calculating current best profit with the lowest price when looping prices.
    O(1) storage, O(n) runtime.
    Beat 43% runtime, 36% storage of all Leetcode submissions.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        low,out = float("inf"),0
        for price in prices:
            if price < low:
                low = price
            else:
                out = max(price-low,out)
        return out

# Tests.
assert(Solution().maxProfit([7,1,5,3,6,4]) == 5)
assert(Solution().maxProfit([7,6,4,3,1]) == 0)
assert(Solution().maxProfit([1]) == 0)
assert(Solution().maxProfit([1,2]) == 1)