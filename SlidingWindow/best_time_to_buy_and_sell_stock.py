class Solution:
    def maxProfit(self, prices) -> int:
        buy_ptr, sell_ptr = 0, 1
        max_profit = 0
        while sell_ptr < len(prices):
            if prices[sell_ptr] > prices[buy_ptr]:
                profit = prices[sell_ptr] - prices[buy_ptr]
                max_profit = max(profit, max_profit)
            else:
                buy_ptr = sell_ptr
            sell_ptr += 1
        return max_profit


test = Solution()
# print(test.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))

# A unique solution I found on LeetCode
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         min_price = float('inf')
#         profit = 0
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif  price - min_price > profit:
#                 profit = price - min_price
#         return profit
