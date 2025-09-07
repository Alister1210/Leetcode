# 121. Best time to buy and sell stocks
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in prices[1:]:
            if i<buy:
                buy = i
            elif i-buy>profit:
                profit = i-buy
        return profit