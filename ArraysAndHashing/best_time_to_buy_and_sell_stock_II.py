# Greedy since you can buy and sell as much as you want
# Time: O(n)
# Space: O(1)
def maxProfit(prices) -> int:
    result = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            result += prices[i] - prices[i - 1]

    return result


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(maxProfit(prices=[1, 2, 3, 4, 5]))
print(maxProfit(prices=[7, 6, 4, 3, 1]))
