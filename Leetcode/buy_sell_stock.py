from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_price:
                max_price = price - min_price
        return max_price

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    buy_sell_stock_obj = Solution()
    output = buy_sell_stock_obj.maxProfit(prices)
    print(output)
