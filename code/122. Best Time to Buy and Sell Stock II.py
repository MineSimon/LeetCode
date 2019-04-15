class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
                continue
            else:
                if i+1 < len(prices) and prices[i+1] < prices[i]:
                    max_profit = max_profit + (prices[i] - min_price)
                    min_price = prices[i+1]

        # 当处于递增情况时退出循环, 没有计算最后一次的收益
        if prices[-1] > min_price:
            max_profit = max_profit + (prices[-1] - min_price)
        return max_profit


class Solutin2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max((prices[i]-prices[i-1]), 0)
        return max_profit
