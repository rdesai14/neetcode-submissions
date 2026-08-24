class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        maxP = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxP = max((prices[sell] - prices[buy]), maxP)
            else:
                buy = sell
            
            sell = sell + 1
        return maxP



        