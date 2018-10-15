#encoding:utf8
__author__ = 'gold'

'''
Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        buyPrice = prices[0]
        profit = 0
        maxProfit = 0
        sellPrice = -1

        index = 1
        while index < len(prices):
            if prices[index] > buyPrice:
                if sellPrice == -1:
                    sellPrice = prices[index]
                    profit = sellPrice - buyPrice
                    if profit > maxProfit:
                        maxProfit = profit
                else:
                    if sellPrice < prices[index]:
                        sellPrice = prices[index]
                        profit = sellPrice - buyPrice
                        if maxProfit < profit:
                            maxProfit = profit
            elif prices[index] < buyPrice:
                buyPrice = prices[index]
                sellPrice = -1
            index += 1
        return maxProfit

if __name__ == '__main__':
    s = [7]
    s = [7,1,5,3,6,4]
    s = [7,6,4,3,1]
    s = [3,2,6,5,0,3]
    print(Solution().maxProfit(s))