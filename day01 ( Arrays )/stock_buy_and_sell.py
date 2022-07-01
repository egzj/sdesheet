# Date Completed: 1st July 2022
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# References:
# 1. https://dxmahata.gitbooks.io/leetcode-python-solutions/content/best_time_to_buy_and_sell_stock.html

###################################################
# more efficient (copied from reference 1)
###################################################
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        else:
            max_profit = 0
            min_price = prices[0]
            for i in range(len(prices)):
                profit = prices[i] - min_price
                max_profit = max(profit, max_profit)
                min_price = min(min_price, prices[i])

            return max_profit

########################
# brute force method
########################
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         index = None
#         maxProfit = 0
#         for x in range(len(prices)):
#             for y in range(x + 1, len(prices)):
#                 if prices[y] - prices[x] > maxProfit:
#                     maxProfit = prices[y] - prices[x]
                    
#         return maxProfit