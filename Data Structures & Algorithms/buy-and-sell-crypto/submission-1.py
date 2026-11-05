class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        brute force : 
         iterate profits
         n-1 + n-2 + ... + n - n  
         n*n - ( 1 + .. + n) 
         n2 - n2 / 2 = o (n2)

        sliding window: 
         start from left, and keep increasing R until profit is increasing. 
         as R reaches end, return max profit

         Tricky input:
         [10,1,5,0,7,2,100] 0->6
        '''

        l, r, max_profit = 0, 0 , 0
        while (r <= len(prices) - 1):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            if profit < 0: 
                l += 1
            else:
                r += 1

        return max_profit