class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPtr = 0
        ptr = 0
        maxProfit = 0 
        while ptr != len(prices):
            profit = prices[ptr] - prices[minPtr]
            if profit > maxProfit: 
                maxProfit = profit
            if prices[ptr] < prices[minPtr]:
                minPtr = ptr 
            ptr += 1

        return maxProfit

        