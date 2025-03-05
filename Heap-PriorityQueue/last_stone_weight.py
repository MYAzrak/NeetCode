import heapq


# Using sorting
# Time: O(n^2logn)
# Space: O(1)
def lastStoneWeight(stones) -> int:
    while len(stones) > 1:
        stones.sort()
        x = stones.pop()
        y = stones.pop()
        if x == y:
            continue
        else:
            stones.append(x - y)

    return stones[0] if stones else 0


# Using heap
# Time: O(nlogn)
# Space: O(n)
def lastStoneWeight(stones) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        result = -heapq.heappop(stones) + heapq.heappop(stones)
        if result != 0:
            heapq.heappush(stones, -result)
    return -stones[0] if stones else 0
