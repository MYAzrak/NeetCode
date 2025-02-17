# Two pointers
# Time: O(N)
# Space: O(1)
def maxProfit(prices) -> int:
    buy_ptr, sell_ptr = 0, 1
    max_profit = 0
    while sell_ptr < len(prices):
        if prices[sell_ptr] > prices[buy_ptr]:
            profit = prices[sell_ptr] - prices[buy_ptr]
            max_profit = max(profit, max_profit)
        else:
            buy_ptr = sell_ptr  # go to the min price
        sell_ptr += 1
    return max_profit


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(maxProfit(prices=[7, 6, 4, 3, 1]))
