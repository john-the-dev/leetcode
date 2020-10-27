# 309. Best Time to Buy and Sell Stock with Cooldown
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
from common import *
class Solution:
    '''
    Dynamic programming, dp[i] = max(dp[i],dp[j]+gain) for each j in [0,i-2], in which gain is the gain assuming buy at prices[j] and sell at prices[i].
    O(n^2) runtime, O(n) storage.
    Beat 5% runtime, 5% storage of all Leetcode submissions.
    Note that the distance is 2 not 1 as we need 1 day for cool down. This adds some complexity in coding, especially when initializing.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for j in range(1,i):
                gain = 0 if prices[j-1] >= prices[i-1] else prices[i-1]-prices[j-1]
                dp[i] = max(dp[i],dp[j-2]+gain) if j >= 2 else max(dp[i],dp[j-1]+gain)
        return dp[n]

# Tests.
assert(Solution().maxProfit([1,2,3,0,2]) == 3)
assert(Solution().maxProfit([1,2,3,2,2,1]) == 2)