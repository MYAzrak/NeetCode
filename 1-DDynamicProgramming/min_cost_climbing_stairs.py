# Similar to "Climbing Stairs"
# Time: O(n)
# Space: O(1)
def minCostClimbingStairs(cost) -> int:
    if len(cost) == 0:
        return 0

    if len(cost) == 1:
        return cost[0]

    one, two = cost[-1], 0
    i = len(cost) - 2

    while i >= 0:
        temp = one
        one = min(cost[i] + one, cost[i] + two)
        two = temp
        i -= 1

    return min(one, two)


# Modifying the cost list directly
def minCostClimbingStairs(cost) -> int:
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])

    return min(cost[0], cost[1])
